from settings import *

text_map = [
    '111111111111',
    'P..........1',
    'P..........1',
    'P..........1',
    'P..........1',
    'P..........1',
    'P..........1',
    '111111111111'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == 'P':
                world_map[(i * TILE, j * TILE)] = 'P'