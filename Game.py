import math
import random
import sys
import time

import pygame as pg
import pygame.freetype as freetype
import pygame_menu

import Boss
from Alien import Alien
from Background import Background
from Bullet import Bullet
from Enemy import Enemy
from EnemyFactory import EnemyFactory
from ItemFactory import ItemFactory
from Explosion import Explosion
from Healthbar import Healthbar
from Item import Item
from Player import Player
from Score import Score

global menu
global screen
global clock


class Game:
    SIZE = width, height = 800, 600
    PLAYER_NAME = "Player"
    isBossAlive = False
    LEVEL = 1

    def __init__(self, background: Background, ):
        self.background = background

    def set_player_name(self, name):
        self.PLAYER_NAME = name

    def start_game_form(self):
        start_game_form = pygame_menu.Menu('', 500, 400, theme=pygame_menu.themes.THEME_DARK)
        start_game_form.add.text_input('Name: ', default='Player', onchange=self.set_player_name)
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

    def scoreboard(self):
        scoreboard = pygame_menu.Menu('Scoreboard', 500, 400,
                                      theme=pygame_menu.themes.THEME_DARK)
        scores = Score.get_scoreboard()
        table = scoreboard.add.table(font_size=20)
        table.default_cell_padding = 8
        table.default_row_background_color = (40, 41, 35)
        table.default_cell_border_color = 'white'
        table.add_row(['Name', 'Date', 'Score'])

        for score in scores['players'][:5]:
            table.add_row([score['name'], score['date'], score['score']])

        scoreboard.add.label('', font_size=3)
        scoreboard.add.button('Return to menu', self.start_menu())

        return scoreboard

    def menu_scoreboard(self):
        scoreboard = pygame_menu.Menu('Scoreboard', 500, 400,
                                      theme=pygame_menu.themes.THEME_DARK)
        scores = Score.get_scoreboard()
        table = scoreboard.add.table(font_size=20)
        table.default_cell_padding = 8
        table.default_row_background_color = (40, 41, 35)
        table.default_cell_border_color = 'white'
        table.add_row(['Name', 'Date', 'Score'])

        for score in scores['players'][:5]:
            table.add_row([score['name'], score['date'], score['score']])

        scoreboard.add.label('', font_size=3)
        scoreboard.add.button('Return to menu', pygame_menu.events.BACK)

        return scoreboard

    def start_menu(self):
        start_menu = pygame_menu.Menu('Welcome', 500, 400,
                                      theme=pygame_menu.themes.THEME_DARK)

        start_menu.add.button('Start Game', self.start_game_form())
        start_menu.add.button('Scoreboard', self.menu_scoreboard())
        start_menu.add.button('About', self.about_menu())
        start_menu.add.button('Quit', pygame_menu.events.EXIT)

        return start_menu

    def initialize(self, menu_object=None):

        global menu
        global screen
        global clock

        pg.init()
        screen = pg.display.set_mode(self.SIZE)
        pg.display.set_icon(pg.image.load('data/sprites/alien.PNG'))
        pg.display.set_caption("Human vs Aliens")
        clock = pg.time.Clock()

        if menu_object is None:
            menu_object = self.start_menu()

        menu = menu_object
        menu.mainloop(screen)

    def exit_game(self):
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
            pg.display.set_caption(str("FPS: {}".format(clock.get_fps())))
            self.exit_game()

    def game_over_screen(self):
        # the last frame is 119
        for i in range(1, 119):
            image_animation = pg.image.load('data/GAME_OVER_SCREEN/frame ({}).jpg'.format(i))
            screen.blit(image_animation, (0, 0))
            pg.display.update()
            clock.tick(30)
            pg.display.set_caption(str("FPS: {}".format(clock.get_fps())))
            self.exit_game()

    def nextLevel(self, points):
        if points == 0:
            points = 1
        return math.floor((1 + math.sqrt(1 + 8 * points / 300)) / 2)

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
        enemies.add(EnemyFactory.build(EnemyFactory.ALIEN, self.LEVEL))

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

        # creating a list of items
        items = pg.sprite.Group()

        # this flag is used to check if the player stops to shoot
        flag_key_up = True

        # this flag is used to check if there is still going collision
        flag_collision = False

        # you have to call this at the start to init the font,
        pg.font.init()
        # get data for Font
        font = freetype.Font("data/Font.ttf", 20)

        time_points = math.ceil(time.time())

        # Game loop
        while 1:
            points = player.kill_count + math.ceil(time.time()) - time_points
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

            # Draw items
            items.draw(screen)

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

            # update all the sprites
            all.update()

            # Increment every bullet position and remove the ones that are out of the screen
            for bullet in bullet_list:
                bullet.update()

            item: Item
            for item in items:
                item.move()
                if player.rect.colliderect(item):
                    player.add_item(item)
                    item.kill()

            # Update player's items
            player.update_item_list()

            if self.LEVEL < self.nextLevel(points):
                self.LEVEL = self.nextLevel(points)
                enemies.add(EnemyFactory.build(EnemyFactory.BOSS, self.LEVEL))

            # Spawn new Enemies
            if not Game.isBossAlive:
                if enemy_reload:
                    enemy_reload = enemy_reload - 1
                elif not int(random.random() * Alien.ODDS):
                    enemies.add(EnemyFactory.build(EnemyFactory.ALIEN, self.LEVEL))
                    enemy_reload = Alien.ALIEN_LOAD_TIME

            # Type hinted Enemy
            enemy: Enemy
            for enemy in enemies:
                enemy.move()

                # Check for collisions between the player and the enemies
                if enemy.rect.colliderect(player) and not flag_collision:
                    player.health -= 1
                    enemy.health -= player.DAMAGE  # Here must be a player damage
                    explosion_list.add(Explosion(enemy))
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                flag_collision = enemy.rect.colliderect(player)

                bullet: Bullet
                for bullet in bullet_list:
                    if enemy.rect.colliderect(bullet):
                        if isinstance(enemy, Boss.Boss):
                            enemy: Boss.Boss
                            enemy.health -= bullet.get_damage()  # Here must be a bullet damage
                            # if the boss is NOT DEAD bullets explode
                            explosion_list.add(Explosion(bullet))
                            bullet.kill()

                            # if the boss IS DEAD, the Boss explodes
                            if enemy.health <= 0:
                                explosion_list.add(Explosion(enemy))
                                enemy.kill()
                                # Points from the Boss
                                player.set_kill_count(player.get_kill_count() + (self.LEVEL * pow(2, self.LEVEL)))
                        else:
                            enemy.health -= bullet.get_damage()  # Here must be a bullet damage
                            # if the enemy is NOT DEAD bullets explode
                            if enemy.health <= 0:
                                explosion_list.add(Explosion(enemy))
                                # Points from the Alien == Alien.health
                                player.set_kill_count(player.get_kill_count() + enemy.get_points())

                                # Spawn Item
                                if random.choices([True, False], cum_weights=(1, 20), k=1)[0]:
                                    print('Item spawned')
                                    items.add(ItemFactory.build(level=self.LEVEL, enemy=enemy))

                                enemy.kill()
                            else:
                                # if the enemy IS DEAD, the enemy explodes
                                explosion_list.add(Explosion(bullet))
                            bullet_list.remove(bullet)

            # if player is DEAD start new game
            if player.health <= 0:
                explosion_list.add(Explosion(player))
                score = Score(self.PLAYER_NAME, player.kill_count + math.ceil(time.time()) - time_points)
                score.save()
                # GAME OVER ANIMATION
                self.game_over_screen()
                break

            # update every explosion
            for explosions in explosion_list:
                explosions.update()

            # Render POINTS on the screen
            font.render_to(screen, (5, 30), "Points: " + str(points),
                           (255, 255, 255))

            # Render LEVEL on the screen
            font.render_to(screen, (0, 520), 'Level: ' + str(self.LEVEL), (255, 255, 255))
            font.render_to(screen, (0, 580), 'Attack Damage: ' + str(player.attack_damage), (255, 255, 255))
            font.render_to(screen, (0, 550), 'Bullet Speed: ' + str(player.BULLET_SPEED), (255, 255, 255))

            # Item bar
            item_pos_x = 555
            item_pos_y = 755
            for item in player.item_list:
                screen.blit(item.image, (item_pos_y, item_pos_x))
                item_pos_x -= 45
                if item_pos_x <= 10:
                    item_pos_y -= 45
                    item_pos_x = 555

            # Shows FPS in the title bar
            clock.tick(60)
            pg.display.set_caption(str("FPS: {}".format(clock.get_fps())))

            dirty = all.draw(screen)
            pg.display.update(dirty)
            pg.display.flip()

        self.initialize(self.scoreboard())
