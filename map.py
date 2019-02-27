# coding: utf-8

""" Module contenant la class Map."""

from constants import CARTE


class Map:

    '''
    class representant l'objet map. Elle a un attribut structure qui pointe 
    une liste vide. Celle ci sera rempli grace a la methode structurize.
    '''

    def __init__(self):
        # Mise en place d'attribut pointant des listes vides pour
        # l'instant mais qui seront complété par la methode load_file.
        self.structure = []
        
    

    def structurize(self):
        '''
        Méthode permettant de charger la structure d'un fichier .txt sous forme
        de liste de listes au sein d'un attribut structure de la classe.
        '''

        with open(CARTE, "r") as carte:
            
            return [self.structure.append(list(line.rstrip("\n"))) for line in carte]

        #for l in map_list:      # Ceci est un test. La boucle for est utilisée 
            #print(l)            # pour afficher ligne par ligne       


if __name__ == "__main__":
    """ _name_ est _main_ si le module est lancé en standalone et non importé
    dans ce cas le bloc indenté s'executera (par exemple pour un test)."""


    jeu = Map()
    jeu.structurize()
    print(jeu.structure)