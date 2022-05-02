import random

import Game
from Enemy import Enemy
import pygame as pg


class Boss(Enemy):
    BOSS_DIMENSIONS = Width, Height = 150, 150

    def __init__(self):
        Enemy.__init__(self)
        self.image = pg.image.load('data/sprites/alien_boss.gif')
        self.image = pg.transform.scale(self.image, (self.BOSS_DIMENSIONS[0], self.BOSS_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = Game.Game.SIZE[0] / 2
        self.rect.y = 0
        self.horizontal_movement = 10
        self.direction = random.choice(['left', 'right'])

    def move(self):
        if self.BOSS_DIMENSIONS[0] == self.rect.x:
            self.direction = 'right'
        if self.rect.x == Game.Game.SIZE[0] - self.BOSS_DIMENSIONS[0] * 2:
            self.direction = 'left'

        if self.direction == 'right':
            if self.rect.x + Enemy.SPEED < Game.Game.SIZE[0] - self.BOSS_DIMENSIONS[0]:
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
            self.horizontal_movement = 30

    def get_width(self):
        return self.BOSS_DIMENSIONS[0]

    def get_height(self):
        return self.BOSS_DIMENSIONS[1]
