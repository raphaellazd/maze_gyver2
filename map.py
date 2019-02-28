# coding: utf-8

""" Module contenant la classe Map."""

import constants


class Map:

    '''
    class representant l'objet map. Elle a un attribut structure qui pointe 
    une liste vide. Celle ci sera rempli grace a la methode structurize.
    '''
    structure = []
    free_paths =[]

    def __init__(self):
        # une liste vide permettant d'acceuillir la structure renvoyé par structurize().
        Map.structure = []
        Map.free_paths =[]
    

    def structurize(self):
        '''
        Méthode permettant de charger la structure d'un fichier .txt sous forme
        de liste de listes au sein d'un attribut structure de la classe.
        '''

        with open(constants.CARTE, "r") as carte:
            # On ajoute à l'attribut structure, on enlève les symboles de retour ligne.
            return [Map.structure.append(list(line.rstrip("\n"))) for line in carte]

    
    def get_free_path(self):
        '''
        Méthode permettant de stocker les positions de passage libre dans la map
        '''
        
        for y, line in enumerate(self.structure):
            for x, char in enumerate(line):
                if char == constants.PATH:
                    Map.free_paths.append((y, x))





if __name__ == "__main__":
    import random
    
    jeu = Map()
    jeu.structurize()
    

    jeu.get_free_path()
    print(Map.free_paths)
    print(random.sample(jeu.free_paths, 3))