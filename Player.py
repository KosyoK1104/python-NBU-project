import pygame as pg


class Player(pg.sprite.Sprite):
    DAMAGE = 30
    SPEED = 10

    def __int__(self, name):
        self.name = name
        self.health = 100
        print('asd')
