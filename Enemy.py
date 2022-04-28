import pygame as pg


class Enemy(pg.sprite.Sprite):
    SPEED = 2.5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

    def move(self):
        pass
