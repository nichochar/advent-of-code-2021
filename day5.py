#!/usr/bin/env python3
import os

GRID_SIZE = 1000


class Coords:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def read(relative_filepath):
    with open(relative_filepath, 'r+') as f:
        data = f.read()
        clean_data = data.strip()
        lines = clean_data.split('\n')

    coords = []
    for line in lines:
        [first_part, second_part] = line.split(' -> ')
        first_nums = first_part.split(',')
        second_nums = second_part.split(',')
        coords.append([
            Coords(first_nums[0], first_nums[1]),
            Coords(second_nums[0], second_nums[1]),
        ])

    return coords


def grid_from_coords(coords):
    grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    for [origin, dest] in coords:
        if origin.x != dest.x and origin.y != dest.y:
            # We are traveling diagonally
            x_step = 1
            y_step = 1
            if origin.x > dest.x:
                x_step = -1
            if origin.y > dest.y:
                y_step = -1
            current_x = origin.x
            current_y = origin.y
            while current_x != dest.x and current_y != dest.y:
                grid[current_x][current_y] += 1
                current_x += x_step
                current_y += y_step
            grid[current_x][current_y] += 1

        elif origin.x == dest.x:
            # We are traveling vertically
            step = 1
            if origin.y > dest.y:
                step = -1
            for j in range(origin.y, dest.y + step, step):
                grid[origin.x][j] += 1

        else:
            # We are traveling horizontally
            step = 1
            if origin.x > dest.x:
                step = -1
            for x in range(origin.x, dest.x + step, step):
                grid[x][origin.y] += 1
    return grid


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")
    coords = read('inputs/day5.txt')

    # First, figure out the size of our grid
    grid = grid_from_coords(coords)

    # Calculate the areas where at least 2 lines overlap
    total_dangerous_spots = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] >= 2:
                total_dangerous_spots += 1

    print("Total dangerous spots (>2 lines overlap):", total_dangerous_spots)
