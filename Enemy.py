import pygame as pg


class Enemy(pg.sprite.Sprite):
    SPEED = 2.5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.health = None
        # self.rect.x = None
        # self.rect.y = None

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
