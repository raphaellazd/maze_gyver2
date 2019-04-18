# coding: utf-8

import map
import hero
import sedatif


if __name__ == "__main__":

    print("Arriverez-vous à faire s'évader McGuy ?")

    game = map.Map()
    game.structurize()
    game.get_free_path()
    game.get_end_pos()

    injection = sedatif.Sedatif(game)

    mcguy = hero.Hero(game, injection)
    mcguy.start_pos()

    injection.get_random_pos()
    injection.disperse_items()

    for l in mcguy.structure:
        print(l)

    loop = 1
    game_over = 0

    while loop:

        direction = input("Quel est votre mouvement ? Pressez une touche \
                            de direction puis Entrée.")

        if direction == "q":

            mcguy.move_left()
            mcguy.check_front_jailer(game)
            if mcguy.check_front_jailer(game):
                loop, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "s":
            mcguy.move_below()
            mcguy.check_front_jailer(game)
            if mcguy.check_front_jailer(game):
                loop, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "d":
            mcguy.move_right()
            mcguy.check_front_jailer(game)
            if mcguy.check_front_jailer(game):
                loop, game_over = 0, 1
            else:
                for l in mcguy.structure:
                    print(l)
                continue

        if direction == "z":
            mcguy.move_above()
            mcguy.check_front_jailer(game)
            if mcguy.check_front_jailer(game):
                loop, game_over = 0, 1
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
