# coding: utf-8

""" Module defining Map class."""

import constants
import pygame


class Map:

    '''
    Class representing a map characterized by its global structure,
    its free passages and its end position. It also manages the loading
    of the images necessary for the graphic layer.

    '''

    def __init__(self):

        self.structure = []
        self.free_paths = []
        self.end_pos = []

        self.wall_spr = pygame.image.load(constants.WALL_IMG).convert()
        self.path_spr = pygame.image.load(constants.PATH_IMG).convert()
        self.finish_spr = pygame.image.load(constants.PATH_IMG).convert()
        self.hero_spr = pygame.image.load(constants.HERO_IMG).convert_alpha()
        self.jailer_spr = pygame.image.load(constants.JAILER_IMG).convert()
        self.finish_spr = pygame.image.load(constants.PATH_IMG).convert()
        self.tube_spr = pygame.image.load(constants.TUBE_IMG).convert()
        self.ether_spr = pygame.image.load(constants.ETHER_IMG).convert()
        self.sting_spr = pygame.image.load(constants.STING_IMG).convert()

    def structurize(self):
        '''
        Method for loading the structure of a .txt file in
         list of lists form, within a structure attribute.
        '''

        with open(constants.MAP, "r") as map:
            return [self.structure.append(list(line.rstrip("\n")))
                    for line in map]

    def display_maze(self, screen):
        '''
        Method for displaying the maze graphically.
        '''

        for pos_y, lines in enumerate(self.structure):
            for pos_x, char in enumerate(lines):
                pix_y = pos_y * constants.SPRITE_SZ
                pix_x = pos_x * constants.SPRITE_SZ

                if char == constants.WALL:
                    screen.blit(self.wall_spr, (pix_x, pix_y))
                if char == constants.PATH:
                    screen.blit(self.path_spr, (pix_x, pix_y))
                if char == constants.HERO:
                    screen.blit(self.hero_spr, (pix_x, pix_y))
                if char == constants.JAILER:
                    screen.blit(self.jailer_spr, (pix_x, pix_y))
                if char == constants.FINISH:
                    screen.blit(self.finish_spr, (pix_x, pix_y))
                if char == constants.STING:
                    screen.blit(self.sting_spr, (pix_x, pix_y))
                if char == constants.TUBE:
                    screen.blit(self.tube_spr, (pix_x, pix_y))
                if char == constants.ETHER:
                    screen.blit(self.ether_spr, (pix_x, pix_y))

    def get_free_path(self):
        '''
        Method for acquiring and storing free passage positions in the map
        '''

        for y, line in enumerate(self.structure):
            for x, char in enumerate(line):
                if char == constants.PATH:
                    self.free_paths.append((y, x))

    def get_end_pos(self):
        '''
        Method for acquiring and storing the end position.
        '''

        for y, line in enumerate(self.structure):
            for x, char in enumerate(line):
                if char == constants.FINISH:
                    self.end_pos.append((y, x))


if __name__ == "__main__":
    pass
