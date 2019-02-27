# coding: utf-8

"""
Module contenant la classe hero, representant le personnage jouable 
du jeu. 
"""

import map
import constants

class Hero:
     
    """
    Classe Hero, celle ci ...
    """

    def __init__(self, pos_x=0, pos_y=0):   # les parametres nommés permette d'etre sur l'origine 
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.structure = [['S', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'], [' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#'], [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#'], ['#', '#', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#'], ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'], ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F']]#map.structure
        self.items = []             # servira plus tard a collecter les objets
        
           

    
    def start_pos(self):

        if self.structure[self.pos_y][self.pos_x] == constants.START:
            self.structure[self.pos_y][self.pos_x] = constants.HERO

    def move_left(self):
        
        """
        NOUVELLE VERSION: On utilise plus une classe Position et on rassemble directement
        les methodes de deplacement et d'acqusition des coordonnées dans la meme methode move_...
        """
        
        if self.pos_x > 0:                                  # n'est pas hors limites
            if self.structure[self.pos_y][self.pos_x-1] != constants.WALL:  # n'est pas un mur
                self.structure[self.pos_y][self.pos_x] = constants.PATH   # remplace par chemin
                self.pos_x -= 1                             # modif. coord
                self.structure[self.pos_y][self.pos_x] = constants.HERO   # insertion hero 

    
    def move_below(self):
        
        if self.pos_y < 15:
            if self.structure[self.pos_y+1][self.pos_x] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO
    
    
    def move_right(self):
        
        if self.pos_x < 15:
            if self.structure[self.pos_y][self.pos_x+1] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_x += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO

    
    def move_above(self):
        
        if self.pos_y > 0:
            if self.structure[self.pos_y-1][self.pos_x] != constants.WALL:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y -= 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO


if __name__ == "__main__":
    mcguy = Hero()
    mcguy.start_pos()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)
    
    mcguy.move_below()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)
    
    mcguy.move_below()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)
    
    mcguy.move_left()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)

    mcguy.move_right()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)

    mcguy.move_above()
    print(mcguy.pos_x)
    print(mcguy.pos_y)
    for l in mcguy.structure:
        print(l)