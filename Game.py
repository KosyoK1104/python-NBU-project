import pygame as pg
import sys

import pygame_menu

from Background import Background
from Menu import Menu
from Score import Score

global menu


class Game:
    SIZE = width, height = 800, 600

    def __init__(self, score: Score, background: Background, menu: Menu):
        self.score = score
        self.background = background
        self.menu = menu

    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def start_the_game(self):
        menu.disable()
        menu.full_reset()
        menu.add.text_input('Name :', default='John Doe')
        print('asdasd')
        pass

    def about_menu(self):
        pass

    def initialize(self):

        pg.init()
        screen = pg.display.set_mode(self.SIZE)
        global menu
        menu = pygame_menu.Menu('Welcome', 500, 400,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Start Game', self.start_the_game)
        menu.add.button('About', self.about_menu)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()

            screen.fill(self.background.BACKGROUND_COLOR)
            pg.display.flip()
