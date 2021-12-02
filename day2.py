#!/usr/bin/env python3
import os


def read(relative_filepath):
    """For day 2, returns an array of commands that looks like:
        [
            ["down", "5"],
            ["up", "3"],
            ...
        ]
    """
    with open(relative_filepath, 'r+') as f:
        data = f.read()
        clean_data = data.strip()
        lines = clean_data.split('\n')

    structured_lines = [line.split(' ') for line in lines if line]
    return structured_lines


def solve1(lines):
    x, y = 0, 0  # X is horizontal position and Y is depth
    for line in lines:
        [direction, val] = line
        if direction == "forward":
            x += int(line[1])
        elif direction == "up":
            y -= int(line[1])
        elif direction == "down":
            y += int(line[1])
        else:
            raise Exception(f"Unexpected direction: '{direction}'")
    print("First solve\nX", x, "Y:", y)
    return x * y


def solve2(lines):
    x, y = 0, 0  # X is horizontal position and Y is depth
    aim = 0
    for line in lines:
        [direction, val] = line
        if direction == "forward":
            y = y + aim * int(val)
            x += 5
        elif direction == "up":
            aim -= int(val)
        elif direction == "down":
            aim += int(val)
        else:
            raise Exception(f"Unexpected direction: '{direction}'")
    print("Second solve\nX:", x, "Y:", y)
    return x * y


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")

    lines = read('inputs/day2.txt')

    result = solve1(lines)
    print(f"Result1 {result}")

    result2 = solve2(lines)
    print(f"Result2 {result2}")
