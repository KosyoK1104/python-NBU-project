import pygame as pg
import sys
import random

import pygame_menu

from Background import Background

global menu
global screen


class Game:
    SIZE = width, height = 800, 600

    def __init__(self, background: Background, ):
        self.background = background

    def start_game_form(self):
        start_game_form = pygame_menu.Menu('', 500, 400, theme=pygame_menu.themes.THEME_DARK)
        start_game_form.add.text_input('Name: ', default='Player')
        start_game_form.add.button('Start', self.start_the_game)
        start_game_form.add.button('Return to menu', pygame_menu.events.BACK)
        return start_game_form

    def about_menu(self):
        about_menu = pygame_menu.Menu('About', 500, 400,
                                      theme=pygame_menu.themes.THEME_DARK)
        about_menu.add.label('Автори:')
        about_menu.add.label('Симеон Попов - F100673')
        about_menu.add.label('Констнатин Костадинов - F99557')
        about_menu.add.vertical_margin(30)
        about_menu.add.button('Return to menu', pygame_menu.events.BACK)
        return about_menu

    def initialize(self):

        global menu
        global screen

        pg.init()
        screen = pg.display.set_mode(self.SIZE)
        menu = pygame_menu.Menu('Welcome', 500, 400,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Start Game', self.start_game_form())
        menu.add.button('About', self.about_menu())
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)

    # The game
    def start_the_game(self):
        menu.disable()
        stars = [
            [random.randint(0, self.SIZE[0]), random.randint(0, self.SIZE[1])]
            for x in range(100)
        ]

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            screen.fill(self.background.BACKGROUND_COLOR)
            screen.blit(self.background.getRandomBackground(), (0, 0))
            starColor = pg.Surface(screen.get_size())
            starColor = starColor.convert()
            starColor.fill((0, 0, 0))
            #
            # for star in stars:
            #     pg.draw.line(starColor,
            #                  (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            #     star[1] = star[1] + 1
            #     if star[1] < 0:
            #         star[0] = random.randint(0, self.SIZE[0])
            #         star[1] = self.SIZE[1]
            for star in stars:
                pg.draw.line(starColor,
                             (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
                star[1] = star[1] + 1
                if star[1] < 0:
                    star[1] = self.SIZE[0]
                    star[0] = random.randint(0, self.SIZE[1])
            screen.blit(starColor, (0, 0))
            pg.display.flip()
