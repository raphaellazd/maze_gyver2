# coding: utf-8

"""
Module containing the hero class.
"""

import constants


class Hero:

    """
    Class Hero, it represents the hero through its coordinates, objects that he
    carry or the structure in which it evolves.
    """

    def __init__(self, map, sedatif, pos_x=0, pos_y=0):

        self.structure = map.structure
        self.end_pos = map.end_pos
        self.sedatif = sedatif
        self.random_pos = sedatif.random_pos

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.items = []             
        self.item_counter = 0

    def start_pos(self):
        """
        Method placing the player on the starting sprite.
        """

        if self.structure[self.pos_y][self.pos_x] == constants.START:
            self.structure[self.pos_y][self.pos_x] = constants.HERO

    def check_front_jailer(self, map):
        """
        Method returning a bool, if True the player is in front of the
        jailer.
        """

        if self.structure[self.pos_y][self.pos_x] == \
                self.structure[map.end_pos[0][0]][map.end_pos[0][1]]:
            return True

    def win_or_lose(self):
        """
        Method returning a bool, if True the player has collected the 3 items
        and the game is won.
        """

        if self.item_counter == 3:
            return True
        else:
            return False

    def move_left(self):
        """
        Left move method and object pickup management.
        """

        if self.pos_x > 0:
            if self.structure[self.pos_y][self.pos_x-1] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_x -= 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF:
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO

    def move_below(self):
        """
        Below move method and object pickup management.
        """

        if self.pos_y < 14:
            if self.structure[self.pos_y+1][self.pos_x] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y += 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF:
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO

    def move_right(self):
        """
        Right move method and object pickup management.
        """

        if self.pos_x < 14:
            if self.structure[self.pos_y][self.pos_x+1] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_x += 1
                if self.structure[self.pos_y][self.pos_x] in \
                        constants.SEDATIF:
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO

    def move_above(self):
        """
        Above move method and object pickup management.
        """

        if self.pos_y > 0:
            if self.structure[self.pos_y-1][self.pos_x] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y -= 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF:
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO


if __name__ == "__main__":
    pass
