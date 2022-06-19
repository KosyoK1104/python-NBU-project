import pygame as pg

from Bullet import Bullet


class Enemy(pg.sprite.Sprite):
    SPEED = 2.5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.health = None

    def kill(self) -> None:
        pass

    def get_points(self):
        pass

    def move(self):
        pass

    def update(self):
        pass

    def get_height(self):
        pass

    def get_width(self):
        pass

    def shoot(self) -> Bullet:
        pass
