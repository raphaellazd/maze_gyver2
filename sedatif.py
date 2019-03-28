# coding: utf-8

import map
import constants
import random


class Sedatif():

    def __init__(self, map):

        self.map = map
        self.structure = map.structure
        self.free_paths = map.free_paths
        self.random_pos = []

    def get_random_pos(self):

        self.random_pos = random.sample(self.free_paths, 3)

    def disperse_items(self):

        self.structure[self.random_pos[0][0]][self.random_pos[0][1]] = \
            constants.TUBE
        self.structure[self.random_pos[1][0]][self.random_pos[1][1]] = \
            constants.STING
        self.structure[self.random_pos[2][0]][self.random_pos[2][1]] = \
            constants.ETHER


def main():
    injection = Sedatif(map)
    print(injection.free_paths)
    injection.get_random_pos()
    print(injection.random_pos)
    injection.disperse_items()
    print(injection.random_pos[1][0])
    print(injection.random_pos[1][1])
    for l in injection.structure:
        print(l)


if __name__ == "__main__":
    main()
