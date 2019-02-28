#coding: utf-8


import map
import hero
import sedatif



    
if __name__ == "__main__":
    
    print("Arriverez-vous à faire s'évader McGuy ?")
    
    
    jeu = map.Map()         # init carte
    jeu.structurize()
    jeu.get_free_path()
    
    mcguy = hero.Hero(jeu)          # init mcguyvers
    mcguy.start_pos()

    piqure = sedatif.Sedatif(jeu)   #init sedatif
    piqure.get_random_pos()
    piqure.disperse_items()
    
    for l in mcguy.structure:   # premier affichage de la carte
        print(l)  
    
    continuer = 1

    while continuer:
        
        direction = input("Quel est votre mouvement ? Pressez une touche de direction puis Entrée.")
        
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
    