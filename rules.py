from state_of_game import *
from settings import *
from math_function import intersections_of_circles
from ball import Ball



def check_create_ball(img_ball, balls, time_game, sec):
    """Function for creating balls according to the time rules"""
    if time_game > 50:
        if sec % 100 == 0:
            count_of_new_ball = 3
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))
    if time_game > 20:
        if sec % 200 == 0:
            count_of_new_ball = 2
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))
    elif time_game > 0:
        if sec % 100 == 0:
            count_of_new_ball = 1
            for i in range(0, count_of_new_ball):
                balls.append(Ball(img_ball))


def check_rules(balls, player, state_of_game):
    """Function for checking the exit of the player and balls outside the game map, as well as the collision of balls with walls"""
    # check out the player's texture output
    if player.x > WIDTH - wall_size:
        player.x = WIDTH - wall_size
    if player.x < wall_size:
        player.x = wall_size
    if player.y > HEIGHT - wall_size:
        player.y = HEIGHT - wall_size
    if player.y < wall_size:
        player.y = wall_size
    # check the collision of the balls to the walls
    for ball in balls:
        if (int(ball.x) >= WIDTH - wall_size - 1):  # or (int(ball.x) <= 120):
            ball.dx *= -1
        if (int(ball.y) >= (HEIGHT - wall_size - 1)) or (int(ball.y) <= wall_size + 1):
            ball.dy *= -1
        if (int(ball.x) <= wall_size - 30):
            balls.remove(ball)
        if intersections_of_circles(ball, player):
            state_of_game.switch(Close)
        for i in range(len(balls) - 1):
            if intersections_of_circles(ball, balls[i]) and ball is not balls[i]:
                ball.angle *= -1
                balls[i].angle *= -1
