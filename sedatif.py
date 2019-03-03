# coding: utf-8


import map
import hero
import constants
import random

class Sedatif():

    def __init__(self, map):
        
        self.map = map  # certainement inutile (ou pas!)
        self.structure = map.structure
        self.free_paths = map.free_paths
        self.random_pos = []
    
    
    def get_random_pos(self):
        
        self.random_pos = random.sample(self.free_paths, 3)

    def disperse_items(self):
        
        self.structure[self.random_pos[0][0]][self.random_pos[0][1]] = constants.TUBE 
        self.structure[self.random_pos[1][0]][self.random_pos[1][1]] = constants.STING
        self.structure[self.random_pos[2][0]][self.random_pos[2][1]] = constants.ETHER



    




def main():
    piqure = Sedatif(map)
    print(piqure.free_paths)
    piqure.get_random_pos()
    print(piqure.random_pos)
    piqure.disperse_items()
    print(piqure.random_pos[1][0])
    print(piqure.random_pos[1][1])
    for l in piqure.structure:
        print(l)


if __name__ == "__main__":
    main()

    
