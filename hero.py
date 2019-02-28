# coding: utf-8

"""
Module contenant la classe hero, representant le personnage jouable 
du jeu. 
"""

import map
import constants

class Hero:
     
    """
    Classe Hero, celle ci represente le heros au travers de ses coordonnées, des objets qu'il
    transporte ou de la structure dans laquelle il evolue.
    """

    def __init__(self, map, pos_x=0, pos_y=0):   # les parametres nommés permette d'etre sur l'origine 
        
        self.map = map
        self.pos_x = pos_x
        self.pos_y = pos_y            # Je n'arrive pas a mettre ici map.structure pour pointer vers l attribut structure de Map
        self.structure = map.structure #[['S', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'], [' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#'], [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#'], ['#', '#', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#'], ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'], ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F']]#map.structure
        self.items = []             # servira plus tard a collecter les objets
        
           

    
    def start_pos(self):

        if self.structure[self.pos_y][self.pos_x] == constants.START:
            self.structure[self.pos_y][self.pos_x] = constants.HERO

    def move_left(self):
        """
        Méthode de mouvement vers la gauche.
        """
        
        if self.pos_x > 0:                                                  # si n'est pas hors limites
            if self.structure[self.pos_y][self.pos_x-1] != constants.WALL:  # si dir n'est pas un mur
                self.structure[self.pos_y][self.pos_x] = constants.PATH     # remplace par chemin
                self.pos_x -= 1                                             # modif. coord
                self.structure[self.pos_y][self.pos_x] = constants.HERO     # insertion hero 

    
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
    print(mcguy.structure)
    #mcguy.start_pos()
    
    """print(mcguy.pos_x)
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
    for l in mcguy.structure:
        print(l)

    mcguy.move_right()
    for l in mcguy.structure:
        print(l)

    mcguy.move_above()
    for l in mcguy.structure:
        print(l)"""