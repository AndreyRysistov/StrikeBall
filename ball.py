import pygame
from settings import *
import math
import random


class Ball:
    """
    Class that implements the mechanics of game balls.
    The class has the following attributes:
        ball_number-a class attribute that is available to all objects in the class. it is used to create a unique ball identifier
        id - unique identifier of the balloon
        object-ball image
        pos tuple consisting of the coordinates of the ball is a pair of random numbers that lie in the map scale range at the time of creating the ball
        shift - offset of the ball when it is displayed on the screen
        scale-the scaling factor
        dx, dy-projections of the ball velocity vector on the direction of the x and Y axes
        angle-the angle at which the balloon flies is set by a random value
        r - radius of the ball
    The class has the following methods:
        locate-determine the position of the ball and its projections on the map
        movement-changing the coordinates of the ball in accordance with the laws of kinematics
    """
    ball_number = 0

    def __init__(self, img):
        Ball.ball_number += 1
        self.id = Ball.ball_number
        self.object = img
        self.pos = self.x, self.y = (random.uniform(7.8, 10.5) * TILE, random.uniform(2.0, 6.5) * TILE)
        self.shift = ball_shift
        self.scale = ball_scale
        self.dx, self.dy = ball_speed
        self.angle = random.uniform(math.pi / 2 + math.pi / 8, 3 * math.pi / 2 - math.pi / 8)
        self.r = ball_radius

    def locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        distance_to_ball = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_ball *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and distance_to_ball < fake_walls[fake_ray][0]:
            proj_height = min(int(PROJ_COEFF / distance_to_ball * self.scale), 2 * HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            ball_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            ball = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_ball, ball, ball_pos)
        else:
            return (False,)

    def movement(self):
        self.x = self.x + self.dx * math.cos(self.angle) * TILE
        self.y = self.y + self.dy * math.sin(self.angle) * TILE
        self.pos = (self.x, self.y)
