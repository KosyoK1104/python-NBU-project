import math
import time

import pygame as pg
import pygame.freetype as freetype
import sys
import random

import pygame_menu

from Score import Score
from EnemyFactory import EnemyFactory
from Alien import Alien
from Enemy import Enemy
from Background import Background
from Player import Player
from Healthbar import Healthbar
from Explosion import Explosion

global menu
global screen
global clock


class Game:
    SIZE = width, height = 800, 600
    PLAYER_NAME = "Player"

    def __init__(self, background: Background, ):
        self.background = background

    def start_game_form(self):
        start_game_form = pygame_menu.Menu('', 500, 400, theme=pygame_menu.themes.THEME_DARK)
        start_game_form.add.text_input('Name: ', default='Player', onchange=self.set_player_name)
        start_game_form.add.button('Start', self.start_the_game)
        start_game_form.add.button('Return to menu', pygame_menu.events.BACK)
        return start_game_form

    def set_player_name(self, name):
        self.PLAYER_NAME = name

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

    @staticmethod
    def exit_game():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def intro(self):
        # the last frame is 254
        for i in range(0, 247):
            image_animation = pg.image.load('data/Gif_Animation/frame_' + str(i) + '_delay-0.05s.jpg')
            image_animation = pg.transform.scale(image_animation, (Game.SIZE[0], Game.SIZE[1]))
            screen.blit(image_animation, (0, 0))
            pg.display.update()
            clock.tick(30)
            self.exit_game()

    # The game
    def start_the_game(self):
        menu.disable()

        # intro animation
        # self.intro()

        enemies = pg.sprite.Group()
        all = pg.sprite.RenderUpdates()

        # Generate random coordinates for the background stars
        stars = [
            [random.randint(0, self.SIZE[0]), random.randint(0, self.SIZE[1])]
            for x in range(100)
        ]
        # Aliens
        enemy_reload = Alien.ALIEN_LOAD_TIME
        enemies.add(EnemyFactory.build(1, 1))

        # Spawning the player
        player = Player()
        player_list = pg.sprite.Group()
        player_list.add(player)

        # Creating a healthbar
        healthbar = Healthbar()

        # creating a list of bullets
        bullet_list = pg.sprite.Group()

        # creating a list of explosions
        explosion_list = pg.sprite.Group()

        # this flag is used to check if the player stops to shoot
        flag_key_up = True

        # you have to call this at the start to init the font,
        pg.font.init()
        # get data for Font
        font = freetype.Font("data/Font.ttf", 20)

        time_points = math.ceil(time.time())
        # Game loop
        while 1:
            # Event handling for EXIT
            self.exit_game()

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
            player.draw(screen)

            # Update the healthbar
            healthbar.update(player)

            # DRAW healthbar
            healthbar.draw(screen)

            # Draw Aliens
            enemies.draw(screen)

            # listens to the events and passes them to the player event handler
            keys = pg.key.get_pressed()
            player.event_handler(keys)

            # listens for the player to shoot < - THIS WORKS BUT NOT CONTROLLABLE
            if keys[pg.K_SPACE]:
                if flag_key_up:
                    fired_bullet = player.shoot()
                    bullet_list.add(fired_bullet)
                    flag_key_up = False
            # if the player stops shooting, we set the flag to true
            else:
                flag_key_up = True

            # DRAW the bullets
            bullet_list.draw(screen)

            # DRAW the explosions
            explosion_list.draw(screen)

            # Increment every bullet position and remove the ones that are out of the screen
            for bullet in bullet_list:
                bullet.update()

            # update all the sprites
            all.update()

            # Spawn new Enemies
            if enemy_reload:
                enemy_reload = enemy_reload - 1
            elif not int(random.random() * Alien.ODDS):
                enemies.add(EnemyFactory.build(1, 1))
                enemy_reload = Alien.ALIEN_LOAD_TIME

            for enemy in enemies:
                enemy.move()

                if enemy.rect.colliderect(player):
                    explosion_list.add(Explosion(enemy))
                    enemies.remove(enemy)
                    player.health -= 1

                if enemy.rect.y + enemy.get_height() > self.SIZE[1]:
                    enemies.remove(enemy)

                for bullet in bullet_list:
                    if enemy.rect.colliderect(bullet):
                        explosion_list.add(Explosion(enemy))
                        enemies.remove(enemy)
                        bullet_list.remove(bullet)
                        player.kill_count += 10

            # if player is DEAD start new game
            if player.health == 0:
                explosion_list.add(Explosion(player))
                # SCOREBOARD DOESN'T WORK PROPPERLY !!! DONT USE IT
                score = Score(Game.PLAYER_NAME, player.kill_count + math.ceil(time.time()) - time_points)
                score.save()
                self.initialize()

            # update every explosion
            for explosions in explosion_list:
                explosions.update()

            font.render_to(screen, (5, 30), "Points: " + str(player.kill_count + math.ceil(time.time()) - time_points), (255, 255, 255))

            # shows fps in the title bar
            clock.tick(60)
            pg.display.set_caption(str("FPS: {}".format(clock.get_fps())))

            dirty = all.draw(screen)
            pg.display.update(dirty)
            pg.display.flip()
