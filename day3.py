#!/usr/bin/env python3
import os


LENGTH = 12


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


def solve(data):
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
    print(f"Half way = {half}")
    bit_len = len(data[0])
    ones_counter = {i: 0 for i in range(bit_len)}
    for line in data:
        for i in range(bit_len):
            elt = line[i]
            if elt == '1':
                ones_counter[i] += 1

    gamma, epsilon = '', ''
    for key, val in ones_counter.items():
        if val > half:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print("epsilon", epsilon)
    print("gamma", gamma)
    return bitsToInt(gamma), bitsToInt(epsilon)


def solve2(data: [str], candidates_fn) -> (int, int):
    """
    Naive solve:
        1) For each bit
        2) Check if previous candidate list length is 1
        3) If yes return, else move to the next bit
        4) Create a new list of candidates
    """
    previous_candidates = data
    for i in range(LENGTH):
        new_candidates = candidates_fn(previous_candidates, i)
        if len(new_candidates) == 1:
            return new_candidates[0]
        previous_candidates = new_candidates

    assert len(new_candidates) == 1, f"len not 1... found {len(new_candidates)}"


def get_candidates_high(sublist, idx_pos):
    """Get candidates takes a sublist of the initial list of
    binary numbers, and an index position.

    Then, given that index position, it considers the most common
    bit in that position, in this sublist.

    Finally, it dismisses all examples that do not hold this bit
    in that position and returns the new list of candidates
    """
    ones = [elt for elt in sublist if elt[idx_pos] == '1']
    zeroes = [elt for elt in sublist if elt[idx_pos] == '0']
    if len(ones) >= len(zeroes):
        keep_ones = True
    else:
        keep_ones = False

    if keep_ones is True:
        return ones
    else:
        return zeroes


def get_candidates_low(sublist, idx_pos):
    ones = [elt for elt in sublist if elt[idx_pos] == '1']
    zeroes = [elt for elt in sublist if elt[idx_pos] == '0']
    if len(zeroes) <= len(ones):
        keep_zeroes = True
    else:
        keep_zeroes = False

    if keep_zeroes is True:
        return zeroes
    else:
        return ones


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]

    print("Testing...")
    assert 22 == bitsToInt('10110')

    print(f"Solving {name} for advent of code")
    data = read('inputs/day3.txt')

    gamma, epsilon = solve(data)
    print(f"Result: gamma ({gamma}) * epsilon ({epsilon}) = {gamma * epsilon}")

    o2 = solve2(data, get_candidates_high)
    co2 = solve2(data, get_candidates_low)
    print(f"Result: o2 ({o2}) * co2 ({co2}) = {int(o2, 2) * int(co2, 2)}")



