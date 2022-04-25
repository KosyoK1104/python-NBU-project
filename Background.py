import pygame as pg


class Background:
    SPEED = 10
    BACKGROUND_COLOR = 23, 43, 5

    def create(self):
        print('asd')

    def getRandomBackground(self) -> pg.Surface:
        # return image
        return pg.image.load('data/sprites/bg.png')


