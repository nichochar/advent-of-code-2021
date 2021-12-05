#!/usr/bin/env python3
import os


def read(relative_filepath):
    """For day 3, returns...
    """
    with open(relative_filepath, 'r+') as f:
        data = f.read()
        clean_data = data.strip()
        lines = clean_data.split('\n')

    return lines


def bitsToInt(bitstring):
    """Takes a string like 10110 and returns its decimal value (22)
    """
    return int(bitstring, 2)


def solve1(data):
    """
    Expects data in the form of a dict of strings:
        [
            '110101',
            '001010',
            ...
        ]

    Returns the most common bit (gamma) and the least
    common bit (epsilon) as a tuple
    """
    num_samples = len(data)
    half = num_samples // 2  # This could give an off by one error
    bit_len = len(data[0])
    ones_counter = {i: 0 for i in range(bit_len)}
    for line in data:
        for i in range(bit_len):
            elt = line[i]
            if elt == '1':
                ones_counter[i] += 1

    gamma, epsilon = '', ''
    for key, val in ones_counter.items():
        print(f"Found {val} ones in {key} position")
        if val > half:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print("epsilon", epsilon)
    print("gamma", gamma)
    return bitsToInt(gamma), bitsToInt(epsilon)


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]

    print("Testing...")
    assert 22 == bitsToInt('10110')

    print(f"Solving {name} for advent of code")
    data = read('inputs/day3.txt')

    gamma, epsilon = solve1(data)
    print(f"Result: gamma ({gamma}) * epsilon ({epsilon}) = {gamma * epsilon}")
