import time

import pygame as pg
import sys
import random

import pygame_menu

from EnemyFactory import EnemyFactory
from Alien import Alien
from Enemy import Enemy
from Background import Background
from Player import Player

global menu
global screen
global clock


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
        global clock

        pg.init()
        screen = pg.display.set_mode(self.SIZE)
        pg.display.set_icon(pg.image.load('data/sprites/alien.PNG'))
        pg.display.set_caption("Human vs Aliens")
        clock = pg.time.Clock()

        menu = pygame_menu.Menu('Welcome', 500, 400,
                                theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Start Game', self.start_game_form())
        menu.add.button('About', self.about_menu())
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)

    def intro(self):
        # the last frame is 254
        for i in range(0, 247):
            image_animation = pg.image.load('data/Gif_Animation/frame_' + str(i) + '_delay-0.05s.jpg')
            image_animation = pg.transform.scale(image_animation, (Game.SIZE[0], Game.SIZE[1]))
            screen.blit(image_animation, (0, 0))
            pg.display.update()
            clock.tick(30)

    # The game
    def start_the_game(self):
        menu.disable()

        # intro animation
        self.intro()
        enemies = pg.sprite.Group()
        all = pg.sprite.RenderUpdates()

        Alien.container = enemies, all

        # Generate random coordinates for the background stars
        stars = [
            [random.randint(0, self.SIZE[0]), random.randint(0, self.SIZE[1])]
            for x in range(100)
        ]

        enemyreload = Alien.ALIEN_LOAD_TIME
        Alien()

        # Spawning the player
        player = Player()
        player_list = pg.sprite.Group()
        player_list.add(player)

        # Game loop
        while 1:
            # Event handling for EXIT
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # Stars background animation
            screen.fill(self.background.BACKGROUND_COLOR)
            screen.blit(self.background.getRandomBackground(), (0, 0))
            starColor = pg.Surface(screen.get_size())
            starColor = starColor.convert()
            starColor.fill((0, 0, 0))

            # Draw stars
            for star in stars:
                pg.draw.line(starColor,
                             (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
                star[1] = star[1] + 1

            # if the star is out of the screen, we put it back to the top
                if star[1] > self.SIZE[1]:
                    star[0] = random.randint(0, self.SIZE[0])
                    star[1] = 0

            screen.blit(starColor, (0, 0))
            all.clear(screen, starColor)

            # DRAW the players (for now only one)
            player_list.draw(screen)

            # listens to the events and passes them to the player event handler
            keys = pg.key.get_pressed()
            player.event_handler(keys)

            # update all the sprites
            all.update()
            if enemyreload:
                enemyreload = enemyreload - 1
            elif not int(random.random() * Alien.ODDS):
                # print('asd')
                Alien()
                enemyreload = Alien.ALIEN_LOAD_TIME

            # shows fps in the title bar
            clock.tick(60)
            pg.display.set_caption(str("FPS: {}".format(clock.get_fps())))

            dirty = all.draw(screen)
            pg.display.update(dirty)
            pg.display.flip()
