# coding: utf-8

import pygame
from pygame import locals
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

    welcome_img = pygame.image.load(constants.WELCOME_IMG).convert()
    win_img = pygame.image.load(constants.WIN_IMG).convert()
    loose_img = pygame.image.load(constants.LOOSE_IMG).convert()

    game = map.Map()
    game.structurize()
    game.get_free_path()
    game.get_end_pos()

    injection = sedatif.Sedatif(jeu)

    mcguy = hero.Hero(jeu, injection)
    mcguy.start_pos()

    injection.get_random_pos()
    injection.disperse_items()

    welcome = 1
    loop = 0
    game_over = 0

    while welcome:

        screen.blit(welcome_img, (0, 0))
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_RETURN:
                    welcome, loop = 0, 1

        pygame.display.flip()

    while loop:

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
                        loop, game_over = 0, 1

                if event.key == locals.K_UP:
                    mcguy.move_above()

        jeu.display_maze(screen)
        pygame.display.flip()

    while game_over:

        if mcguy.win_or_lose():
            screen.blit(win_img, (96, 96))

        else:
            screen.blit(loose_img, (96, 96))

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
            if event.type == locals.KEYDOWN:
                if event.key == locals.K_q:
                    game_over = 0

        pygame.display.flip()


if __name__ == "__main__":
    main()
