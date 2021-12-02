#!/usr/bin/env python3
import os


def read(relative_path):
    with open(relative_path, 'r') as f:
        data = f.read()
        lines = data.strip().split('\n')

    lines = [int(elt) for elt in lines if elt]
    return lines


def solve(lines):
    count = 0
    for i in range(len(lines) - 1):
        current = lines[i]
        next_ = lines[i + 1]
        if current < next_:
            count += 1
    print(current, next_)
    return count


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")

    lines = read('inputs/day1.txt')
    result = solve(lines)
    print(f"Result: {result}")
