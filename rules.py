from state_of_game import *
from settings import *
from ball import Ball
from player import Player
import math

def distance(a, b):
    distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    return distance


def intersections_of_circles(a, b):
    intersection = True if a.r - b.r < distance(a, b) < a.r + b.r else False
    return intersection


def check_rules(balls, player, state_of_game, time):
    for ball in balls:
        if (int(ball.x) >= WIDTH - 120):  # or (int(self.x) <= 120):
            ball.dx *= -1
        if (int(ball.y) >= (HEIGHT - 120)) or (int(ball.y) <= 120):
            ball.dy *= -1
        if (int(ball.x) <= 100):
            balls.remove(ball)
        if intersections_of_circles(ball, player):
            state_of_game.switch(Close)
