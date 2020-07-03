import pygame

from player import Player
from ball import Ball
from drawing import Drawing
from state_of_game import *
from settings import *

from ray_casting import ray_casting
from rules import check_rules

pygame.init()
pygame.display.set_caption("Robot and balls")
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
img_ball = pygame.image.load(ball_img).convert_alpha()

time_game = 0
sec = 0
balls = [Ball(img_ball) for i in range(0, count_of_ball)]
player = Player()
drawing = Drawing(sc, sc_map)
state_of_game = Running()
start_time = pygame.time.get_ticks()

while True:
        if state_of_game.name == 'running':
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                        state_of_game.switch(Pause)
                if keys[pygame.K_BREAK]:
                        state_of_game.switch(Close)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                exit()
                if sec % 100 == 0:
                        balls.append(Ball(img_ball))
                clock.tick(60)
                time_game = (pygame.time.get_ticks() - start_time) // 1000
                player.movement()
                [ball.movement() for ball in balls]
                walls = ray_casting(player, drawing.textures)

                drawing.fill(BLACK)
                drawing.background(player.angle)
                drawing.world(walls + [ball.locate(player, walls) for ball in balls])
                drawing.fps(clock)
                drawing.timer(time_game)
                drawing.mini_map(player, balls)
                pygame.display.flip()
                check_rules(balls, player, state_of_game, time_game)
                sec += 1
        elif state_of_game.name == 'close':
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                        start_time = pygame.time.get_ticks()
                        balls = [Ball(img_ball) for i in range(0, count_of_ball)]
                        player = Player()
                        state_of_game.switch(Running)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                exit()
                drawing.fill(BLACK)
                drawing.print_text('Game over', (HALF_WIDTH - 100, HALF_HEIGHT - 100), WHITE)
                drawing.print_text('Your time: {}'.format(time_game), (HALF_WIDTH + 150, HALF_HEIGHT + 150), WHITE)
                pygame.display.flip()
        elif state_of_game.name == 'pause':
                pygame.time.wait(1)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                        state_of_game.switch(Running)
                if keys[pygame.K_BREAK]:
                        state_of_game.switch(Close)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                exit()


