import pygame as pg

from Enemy import Enemy


class Alien(Enemy):
    ODDS = 13
    ALIEN_LOAD_TIME = 60

    def __int__(self):
        Enemy.__init__(self, self.container)
        self.image = pg.image.load('data/sprites/alien.PNG')
        self.rect = self.image.get_rect()

    @staticmethod
    def decrease(self):
        self.ALIEN_LOAD_TIME = self.ALIEN_LOAD_TIME - 1
