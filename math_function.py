from settings import *
import math


def mapping(a, b):
    """Function for mapping"""
    return (a // TILE) * TILE, (b // TILE) * TILE

def distance(a, b):
    """Function for calculating the Euclidean distance between points a and b"""
    distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    return distance

def intersections_of_circles(a, b):
    """Function for determining the intersection of two circles defined by their own radius"""
    intersection = True if a.r - b.r < distance(a, b) < a.r + b.r else False
    return intersection
