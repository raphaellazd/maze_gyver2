# coding: utf-8

import pygame
import map
import hero
import sedatif
import constants


def main():

    pygame.init()

    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Maze Gyver")

    pygame.mixer.music.load("theme.mp3")
    pygame.mixer.music.play(-1)

    gagne = pygame.image.load(constants.GAGNE_IMG).convert()
    perdu = pygame.image.load(constants.PERDU_IMG).convert()

    jeu = map.Map()
    jeu.structurize()
    jeu.get_free_path()
    jeu.get_end_pos()

    piqure = sedatif.Sedatif(jeu)

    mcguy = hero.Hero(jeu, piqure)
    mcguy.start_pos()

    piqure.get_random_pos()
    piqure.disperse_items()

    continuer = 1
    game_over = 0

    while continuer:

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_LEFT:
                    mcguy.move_left()
                if event.key == locals.K_DOWN:
                    mcguy.move_below()
                if event.key == locals.K_RIGHT:
                    mcguy.move_right()
                    if mcguy.check_front_jailer(jeu):
                        continuer, game_over = 0, 1

                if event.key == locals.K_UP:
                    mcguy.move_above()

        jeu.display_maze(screen)
        pygame.display.flip()

    while game_over:

        if mcguy.win_or_lose():
            screen.blit(gagne, (96, 96))

        else:
            screen.blit(perdu, (96, 96))

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_q:
                    game_over = 0

        pygame.display.flip()


if __name__ == "__main__":
    main()
