import pygame as pg

from Enemy import Enemy


class Alien(Enemy):
    def __int__(self):
        super()
        self.image = pg.image.load('data/sprites/alien.PNG')
        self.rect = self.image.get_rect()
