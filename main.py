#coding: utf-8


import map
import hero

if __name__ == "__main__":
    
    print("Arriverez-vous à faire s'évader McGuy ?")
    
    
    jeu = map.Map()         # init carte
    jeu.structurize()
    
    mcguy = hero.Hero()          # init mcguyver
    mcguy.start_pos()
    
    for l in mcguy.structure:
            print(l)
    
    continuer = 1

    while continuer:
        
        direction = input("Quel est votre mouvement ? ")
        
        if direction == "q":
            mcguy.move_left()
            for l in mcguy.structure:
                print(l)
            continue
        
        if direction == "s":
            mcguy.move_below()
            for l in mcguy.structure:
                print(l)
            continue
        
        if direction == "d":
            mcguy.move_right()
            for l in mcguy.structure:
                print(l)
            continue
        
        if direction == "z":
            mcguy.move_above()
            for l in mcguy.structure:
                print(l)
            continue

        else:
            #raise exception : la touche n'est pas valide
            pass
    

    
    
    