import pygame
import os
from drawing import Drawing
from logger import Logger
from player import Player
from ray_casting import ray_casting
from rules import *

pygame.init()
#os.environ['SDL_VIDEO_CENTERED'] = '0'#for centering of game window
pygame.display.set_caption("Robot and balls")
sc = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
img_ball = pygame.image.load(ball_img).convert_alpha()


time_game = 0
sec = 0
balls = list()
player = Player()
drawing = Drawing(sc, sc_map)
logger = Logger()
logger.create_data_frame()
state_of_game = Running()
start_time = pygame.time.get_ticks()
temp_time = start_time
while True:
        if state_of_game.name == 'running':
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                        state_of_game.switch(Pause)
                if keys[pygame.K_BREAK]:
                        state_of_game.switch(Close)
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                                logger.log_to_excel()
                                drawing.graphics(logger.df)
                                exit()
                clock.tick(60)
                time_game = (pygame.time.get_ticks() - start_time) // 1000
                player.movement()
                [ball.movement() for ball in balls]
                walls = ray_casting(player, drawing.textures)
                drawing.fill(BLACK)
                drawing.background(player.angle)
                drawing.world(walls + [ball.locate(player, walls) for ball in balls])
                drawing.fps(clock)
                drawing.print_text('time:{}'.format(time_game), TIME_POS, BLACK, 32)
                drawing.mini_map(player, balls)
                pygame.display.flip()
                check_rules(balls, player, state_of_game)
                check_create_ball(img_ball, balls, time_game, sec)
                if (pygame.time.get_ticks() - temp_time)//1000 >= 1.0:
                        for ball in balls:
                                logger.log_to_data_frame(time_game, player, ball)
                        temp_time = pygame.time.get_ticks()
                sec += 1
        elif state_of_game.name == 'close':
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                        start_time = pygame.time.get_ticks()
                        balls = list()
                        player = Player()
                        state_of_game.switch(Running)
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                                drawing.graphics(logger.df)
                                logger.log_to_excel()
                                exit()
                drawing.fill(BLACK)
                drawing.print_text('Game over', (HALF_WIDTH - 100, HALF_HEIGHT - 100), WHITE, 54)
                drawing.print_text('Your time: {}'.format(time_game), (HALF_WIDTH + 150, HALF_HEIGHT + 150), WHITE, 54)
                drawing.print_text('Press ENTER to restart', (WIDTH//2, HEIGHT - HALF_HEIGHT//4), WHITE, 32)
                pygame.display.flip()

        elif state_of_game.name == 'pause':
                pygame.time.wait(1)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                        state_of_game.switch(Running)
                if keys[pygame.K_BREAK]:
                        state_of_game.switch(Close)
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                                logger.log_to_excel()
                                drawing.graphics(logger.df)
                                exit()

