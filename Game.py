import pygame as pg
import sys

import pygame_menu

from Background import Background
from Score import Score

global menu


class Game:
    SIZE = width, height = 800, 600

    def __init__(self, score: Score, background: Background, ):
        self.score = score
        self.background = background

    def start_the_game(self):
        menu.disable()

    def start_game_form(self):
        start_game_form = pygame_menu.Menu('', 500, 400, theme=pygame_menu.themes.THEME_DARK)
        start_game_form.add.text_input('Name: ', default='Player')
        start_game_form.add.button('Start', self.start_the_game)
        start_game_form.add.button('Return to menu', pygame_menu.events.BACK)
        # start the game flow
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

        pg.init()
        screen = pg.display.set_mode(self.SIZE)
        global menu

        menu = pygame_menu.Menu('Welcome', 500, 400,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Start Game', self.start_game_form())
        menu.add.button('About', self.about_menu())
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()

            screen.fill(self.background.BACKGROUND_COLOR)
            pg.display.flip()
