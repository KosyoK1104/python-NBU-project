import random

import pygame as pg

from Enemy import Enemy
import Game


class Alien(Enemy):
    ODDS = 17
    ALIEN_LOAD_TIME = 60
    ALIEN_DIMENSIONS = Width, Height = 80, 80

    def __init__(self, sprite):
        Enemy.__init__(self)
        self.image = pg.image.load(sprite)
        self.image = pg.transform.scale(self.image, (self.ALIEN_DIMENSIONS[0], self.ALIEN_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 720)
        self.rect.y = 0
        self.horizontal_movement = 60
        self.direction = random.choice(['left', 'right'])

    @staticmethod
    def decrease(self):
        self.ALIEN_LOAD_TIME = self.ALIEN_LOAD_TIME - 1

    # TODO implement border for the aliens
    def move(self):
        if self.ALIEN_DIMENSIONS[0] == self.rect.x:
            self.direction = 'right'
        if self.rect.x == Game.Game.SIZE[0] - self.ALIEN_DIMENSIONS[0] * 2:
            self.direction = 'left'

        if self.direction == 'right':
            if self.rect.x + Enemy.SPEED < Game.Game.SIZE[0] - self.ALIEN_DIMENSIONS[0]:
                self.rect.x += Enemy.SPEED
            else:
                self.direction = 'left'

        if self.direction == 'left':
            if self.rect.x - Enemy.SPEED > 0 + 10:
                self.rect.x -= Enemy.SPEED
            else:
                self.direction = 'right'

        self.horizontal_movement -= 1

        if self.horizontal_movement == 0:
            self.direction = random.choice(['left', 'right'])
            self.horizontal_movement = 60

        self.rect.y += 1

    def get_width(self):
        return self.ALIEN_DIMENSIONS[0]

    def get_height(self):
        return self.ALIEN_DIMENSIONS[1]
