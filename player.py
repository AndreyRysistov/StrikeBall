from settings import *
import pygame
import math


class Player:
    """
    Class that implements the player's(robot's) mechanics)
    The class has the following attributes:
        x, y-coordinates of the player on the plane
        angle-the angle of the player's view direction
        r-the player's radius
    The class has the following methods
        pos-returns a tuple consisting of the player's coordinates
        movement-changes the player's coordinates according to the keys pressed on the keyboard
    """

    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.r = player_map_radius

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= player_angle_speed
        if keys[pygame.K_RIGHT]:
            self.angle += player_angle_speed
        self.angle %= DOUBLE_PI
