import pygame
from settings import *
from map import mini_map
import matplotlib.pyplot as plt
import seaborn as sns
class Drawing:
    """
    Class that implements displaying a model of the playing field,
    its component, as well as graphs of the movement of game objects
    The class has the following attributes:
        sc-game window;
        sc_map-mini-map window;
        textures - dictionary with game textures that are located in the img folder.
    The class has the following methods:
        fill-fills the game window with a certain color;
        background-draws the game background;
        world-draws objects that participate in the game mechanics;
        mini_map-draws a mini-map;
        print_text-adds text of the specified format to the screen;
        fps-adds FPS games to the screen;
        graphics - grafics-displays graphs of the player's movement and balls on the screen
    """
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.textures = {'1': pygame.image.load('img/wall4.png').convert(),
                         'P': pygame.image.load('img/portal5.png').convert_alpha(),
                         'S': pygame.image.load('img/sky3.png').convert(),
                         }

    def fill(self, color):
        self.sc.fill(color)

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        self.print_text(display_fps, FPS_POS, DARKORANGE, 32)

    def mini_map(self, player, balls):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        map_ball_list = [(int(ball.x // MAP_SCALE), int(ball.y // MAP_SCALE)) for ball in balls]
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, GREEN, (int(map_x), int(map_y)), player_map_radius)
        for map_ball in map_ball_list:
            pygame.draw.circle(self.sc_map, RED, map_ball, ball_map_radius)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

    def print_text(self, text, text_pos, color, size):
        font_text = pygame.font.SysFont('Arial', size, bold=True)
        render = font_text.render(text, 0, color)
        self.sc.blit(render, text_pos)

    def graphics(self, data):
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        sns.lineplot(x='time', y='player_x', data=data, ax=axes[0][0])
        sns.lineplot(x='time', y='player_y', data=data, ax=axes[0][1])
        sns.lineplot(x='time', y='ball_x', data=data, hue='ball_id', ax=axes[1][0])
        sns.lineplot(x='time', y='ball_y', data=data, hue='ball_id', ax=axes[1][1])
        plt.show()