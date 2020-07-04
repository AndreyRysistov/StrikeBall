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

def check_create_ball(img_ball, balls, time_game, sec):
    if time_game > 50:
        if sec % 100 == 0:
            count_of_new_ball = 3
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))
    if time_game > 15:
        if sec % 200 == 0:
            count_of_new_ball = 2
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))
    elif time_game > 3:
        if sec % 100 == 0:
            count_of_new_ball = 1
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))
def check_rules(balls, player, state_of_game):
    for ball in balls:
        if (int(ball.x) >= WIDTH - 120):  # or (int(self.x) <= 120):
            ball.dx *= -1
        if (int(ball.y) >= (HEIGHT - 120)) or (int(ball.y) <= 120):
            ball.dy *= -1
        if (int(ball.x) <= 100):
            balls.remove(ball)
        if intersections_of_circles(ball, player):
            state_of_game.switch(Close)
