# Script to create the folders needed to hold 2022 solutions

import os

with open('solutions.txt', 'r') as f:
    for name in f.read().split():
        path = os.path.join(os.getcwd(), 'day'+name)

        print(f'Creating {path}')

        os.mkdir(path)
