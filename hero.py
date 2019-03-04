# coding: utf-8

"""
Module contenant la classe hero, representant le personnage jouable 
du jeu. 
"""

import map
import sedatif
import constants
import main

class Hero:
     
    """
    Classe Hero, celle ci represente le heros au travers de ses coordonnées, des objets qu'il
    transporte ou de la structure dans laquelle il evolue.
    """

    def __init__(self, map, sedatif, pos_x=0, pos_y=0):   # les parametres nommés permette d'etre sur l'origine 
                                                        # mais a voir si la fonction start_pos fait pas deja le boulot
        self.map = map
        self.structure = map.structure
        self.end_pos = map.end_pos
        self.sedatif = sedatif
        self.random_pos = sedatif.random_pos
        
        self.pos_x = pos_x
        self.pos_y = pos_y            
        
        self.items = []             # servira plus tard a collecter les objets
        self.item_counter = 0
        
           

    
    def start_pos(self):

        if self.structure[self.pos_y][self.pos_x] == constants.START:
            self.structure[self.pos_y][self.pos_x] = constants.HERO

    '''def gather_items(self):
        
        if self.structure[self.pos_y][self.pos_x] == constants.TUBE or constants.STING or constants.ETHER :
            self.items.append(self.structure[self.pos_y][self.pos_x])
            self.item_counter += 1
            self.structure[self.pos_y][self.pos_x] = constants.PATH'''
    
    def check_front_jailer(self, map): 

        if self.structure[self.pos_y][self.pos_x] == self.structure[map.end_pos[0][0]][map.end_pos[0][1]]:
            return True        
    
    
    def win_or_lose(self):
        
        #if len(self.items) == 3 :
        if self.item_counter == 3 :
            return True
        else :
            return False
            
    #def is_open_path(self):
        
                    
    def move_left(self):
        """
        Méthode de mouvement vers la gauche.
        """
        
        if self.pos_x > 0:                                                  # si n'est pas hors limites
            if self.structure[self.pos_y][self.pos_x-1] != constants.WALL :#or constants.JAILER:  # si dir n'est pas un mur
                self.structure[self.pos_y][self.pos_x] = constants.PATH     # remplace par chemin
                self.pos_x -= 1                                             # modif. coord
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF :
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO     # insertion hero 

    
    def move_below(self):
        
        if self.pos_y < 14:
            if self.structure[self.pos_y+1][self.pos_x] != constants.WALL :#or constants.JAILER:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y += 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF :
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO
    
    
    def move_right(self):
        
        if self.pos_x < 14:
            if self.structure[self.pos_y][self.pos_x+1] != constants.WALL :#or constants.JAILER:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_x += 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF :
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO

    
    def move_above(self):
        
        if self.pos_y > 0:
            if self.structure[self.pos_y-1][self.pos_x] != constants.WALL :#or constants.JAILER:
                self.structure[self.pos_y][self.pos_x] = constants.PATH
                self.pos_y -= 1
                if self.structure[self.pos_y][self.pos_x] in constants.SEDATIF :
                    self.items.append(self.structure[self.pos_y][self.pos_x])
                    self.item_counter += 1
                self.structure[self.pos_y][self.pos_x] = constants.HERO


if __name__ == "__main__":
    pass