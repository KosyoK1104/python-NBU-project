import pygame as pg

import Game
from exceptions.ImageNotLoaded import ImageNotLoadedException


class Healthbar(pg.sprite.Sprite):
    HEALTHBAR_DIMENSIONS = (250, 35)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/healthbar/10.png")
        self.image = pg.transform.scale(self.image,
                                        (Healthbar.HEALTHBAR_DIMENSIONS[0], Healthbar.HEALTHBAR_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = Game.Game.SIZE[0] - Healthbar.HEALTHBAR_DIMENSIONS[0]
        self.rect.y = 10

    def update(self, player):
        try:
            self.image = pg.image.load("data/sprites/healthbar/" + str(player.health) + ".png")
            self.image = pg.transform.scale(self.image,
                                            (Healthbar.HEALTHBAR_DIMENSIONS[0], Healthbar.HEALTHBAR_DIMENSIONS[1]))
            self.rect = self.image.get_rect()
            self.rect.x = -10
            self.rect.y = -4
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
