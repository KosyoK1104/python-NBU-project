import pygame as pg


class Health(pg.sprite.Sprite):
    def __init__(self, health_points: int):
        pg.sprite.Sprite.__init__(self)
        self.rect.x = 0
        self.rect.y = 0
        self.health_points = health_points
