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
    #check out the player's texture output
    if player.x > WIDTH - wall_size:
        player.x = WIDTH - wall_size
    if player.x < wall_size:
        player.x = wall_size
    if player.y > HEIGHT - wall_size:
        player.y = HEIGHT - wall_size
    if player.y < wall_size:
        player.y = wall_size
    #check the collision of the balls to the walls
    for ball in balls:
        if (int(ball.x) >= WIDTH - wall_size-1):  # or (int(ball.x) <= 120):
            ball.dx *= -1
        if (int(ball.y) >= (HEIGHT - wall_size -1)) or (int(ball.y) <= wall_size+1):
            ball.dy *= -1
        if (int(ball.x) <= wall_size - 30):
            balls.remove(ball)
        if intersections_of_circles(ball, player):
            state_of_game.switch(Close)
        for i in range(len(balls)-1):
            if intersections_of_circles(ball, balls[i]) and ball is not balls[i]:
                ball.angle *= -1
                balls[i].angle *= -1