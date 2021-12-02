#!/usr/bin/env python3
import os


def read(relative_path):
    with open(relative_path, 'r') as f:
        data = f.read()
        lines = data.strip().split('\n')

    lines = [int(elt) for elt in lines if elt]
    return lines


def solve1(lines):
    count = 0
    for i in range(len(lines) - 1):
        current = lines[i]
        next_ = lines[i + 1]
        if current < next_:
            count += 1
    print(current, next_)
    return count


def solve2(lines):
    count = 0
    last_sum = 10 ** 3
    for i in range(len(lines) - 2):
        current_sum = lines[i] + lines[i+1] + lines[i+2]
        if i < 3:
            print(i)
            print(current_sum)
        if current_sum > last_sum:
            count += 1
        last_sum = current_sum
    return count


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")

    lines = read('inputs/day1.txt')
    result1 = solve1(lines)
    print(f"Result: {result1}")

    result2 = solve2(lines)
    print(f"Result: {result2}")
