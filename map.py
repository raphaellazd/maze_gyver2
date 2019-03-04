# coding: utf-8

""" Module contenant la classe Map."""

import constants



class Map:

    '''
    class representant l'objet map. Elle a un attribut structure qui pointe 
    une liste vide. Celle ci sera rempli grace a la methode structurize.
    '''
    

    def __init__(self):
        # une liste vide permettant d'acceuillir la structure renvoyé par structurize().
        
        self.structure = []
        self.free_paths = []
        self.end_pos = [] 
        
        self.wall_spr = pygame.image.load(constants.WALL_IMG).convert_alpha()
        self.path_spr = pygame.image.load(constants.PATH_IMG).convert_alpha()
        self.finish_spr = pygame.image.load(constants.PATH_IMG).convert_alpha()
        self.hero_spr = pygame.image.load(constants.HERO_IMG).convert_alpha()
        self.jailer_spr = pygame.image.load(constants.JAILER_IMG).convert_alpha()
        self.finish_spr = pygame.image.load(constants.PATH_IMG).convert_alpha()
        self.tube_spr = pygame.image.load(constants.TUBE_IMG).convert_alpha()
        self.ether_spr = pygame.image.load(constants.ETHER_IMG).convert_alpha()
        self.sting_spr = pygame.image.load(constants.STING_IMG).convert_alpha()


    def structurize(self):
        '''
        Méthode permettant de charger la structure d'un fichier .txt sous forme
        de liste de listes au sein d'un attribut structure.
        '''

        with open(constants.CARTE, "r") as carte:
            # On ajoute à l'attribut structure, on enlève les symboles de retour ligne.
            return [self.structure.append(list(line.rstrip("\n"))) for line in carte]

    
    def display_maze(self, screen):     
        
        for pos_y, lines in enumerate(self.structure) :
            for pos_x, char in enumerate(lines) :
                pix_y = pos_y * constants.SPRITE_SZ
                pix_x = pos_x * constants.SPRITE_SZ 
                
                if char == constants.WALL :
                    screen.blit(self.wall_spr, (pix_x, pix_y))
                if char == constants.PATH :
                    screen.blit(self.path_spr, (pix_x, pix_y))
                if char == constants.HERO :
                    screen.blit(self.hero_spr, (pix_x, pix_y))
                if char == constants.JAILER :
                    screen.blit(self.jailer_spr, (pix_x, pix_y))
                if char == constants.FINISH :
                    screen.blit(self.finish_spr, (pix_x, pix_y))
    
    def get_free_path(self):
        '''
        Méthode permettant de stocker les positions de passage libre dans la map
        '''
        
        for y, line in enumerate(self.structure):
            for x, char in enumerate(line):
                if char == constants.PATH:
                    self.free_paths.append((y, x))


    def get_end_pos(self):

        for y, line in enumerate(self.structure):
            for x, char in enumerate(line):
                if char == constants.FINISH:
                    self.end_pos.append((y, x))






if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    pygame.init()

    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Maze Gyver")
    
    jeu = Map()
    jeu.structurize()
    jeu.display_maze(screen)
    
    while True :
         
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()

        jeu.display_maze(screen)
        pygame.display.flip()