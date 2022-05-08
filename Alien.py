import random

import pygame as pg

import Game
from Enemy import Enemy
from ImageNotLoaded import ImageNotLoadedException


class Alien(Enemy):
    ODDS = 17
    ALIEN_LOAD_TIME = 60
    ALIEN_DIMENSIONS = Width, Height = 80, 80

    def __init__(self, sprite, level):
        try:
            Enemy.__init__(self)
            self.image = pg.image.load(sprite)
            self.image = pg.transform.scale(self.image, (self.ALIEN_DIMENSIONS[0], self.ALIEN_DIMENSIONS[1]))
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, 720)
            self.rect.y = 0
            self.horizontal_movement = 60
            self.direction = random.choice(['left', 'right'])
            self.health = level*10
            self.points = self.health
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

    @staticmethod
    def decrease(self):
        self.ALIEN_LOAD_TIME = self.ALIEN_LOAD_TIME - 1

    def move(self):
        pass

    # TODO implement border for the aliens
    def kill(self) -> None:
        pg.sprite.Sprite.kill(self)

    def get_points(self) -> int:
        return self.points

    def get_width(self):
        return self.ALIEN_DIMENSIONS[0]

    def get_height(self):
        return self.ALIEN_DIMENSIONS[1]
