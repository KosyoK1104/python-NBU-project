from Enemy import Enemy
import pygame as pg


class Boss(Enemy):
    def __int__(self):
        super()
        self.image = pg.image.load('data/sprites/alien_boss.gif')
        self.rect = self.image.get_rect()
