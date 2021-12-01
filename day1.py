#!/usr/bin/env python3
import os


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    print(f"Solving {name} for advent of code")
