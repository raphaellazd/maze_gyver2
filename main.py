# coding: utf-8

import map
import hero
import sedatif


if __name__ == "__main__":

    print("Arriverez-vous à faire s'évader McGuy ?")

    jeu = map.Map()
    jeu.structurize()
    jeu.get_free_path()
    jeu.get_end_pos()

    piqure = sedatif.Sedatif(jeu)

    mcguy = hero.Hero(jeu, piqure)
    mcguy.start_pos()

    piqure.get_random_pos()
    piqure.disperse_items()

    for l in mcguy.structure:
        print(l)

    continuer = 1
    game_over = 0

    while continuer:

        direction = input("Quel est votre mouvement ? Pressez une touche \
                            de direction puis Entrée.")

        if direction == "q":

            mcguy.move_left()
            mcguy.check_front_jailer(jeu)
            if mcguy.check_front_jailer(jeu):
                continuer, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "s":
            mcguy.move_below()
            mcguy.check_front_jailer(jeu)
            if mcguy.check_front_jailer(jeu):
                continuer, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "d":
            mcguy.move_right()
            mcguy.check_front_jailer(jeu)
            if mcguy.check_front_jailer(jeu):
                continuer, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "z":
            mcguy.move_above()
            mcguy.check_front_jailer(jeu)
            if mcguy.check_front_jailer(jeu):
                continuer, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

    while game_over:

        for l in mcguy.structure:
            print(l)

        mcguy.win_or_lose()

        if mcguy.win_or_lose() is True:
            print("gagné")
            print(mcguy.items)
            print(mcguy.item_counter)

        elif mcguy.win_or_lose() is False:
            print("perdu")
            print(mcguy.items)
            print(mcguy.item_counter)

        game_over = 0
