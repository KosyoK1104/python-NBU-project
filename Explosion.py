import pygame as pg

from exceptions.ImageNotLoaded import ImageNotLoadedException


class Explosion(pg.sprite.Sprite):
    EXPLOSION_DIMENSIONS = (200, 200)

    def __init__(self, obj) -> None:
        try:
            pg.sprite.Sprite.__init__(self)
            self.EXPLOSION_DIMENSIONS = ((obj.rect.w * 2) + 40, (obj.rect.h * 2) + 40)
            self.image = pg.image.load("data/Explosion/1.png").convert_alpha()
            self.image = pg.transform.scale(self.image,
                                            (self.EXPLOSION_DIMENSIONS[0], self.EXPLOSION_DIMENSIONS[1])).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = obj.rect.center
            self.frame = 26
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

    def update(self) -> None:
        try:
            self.image = pg.image.load("data/Explosion/{}.png".format(self.frame)).convert_alpha()
            self.image = pg.transform.scale(self.image, (self.EXPLOSION_DIMENSIONS[0], self.EXPLOSION_DIMENSIONS[1]))
            if self.frame < 63:
                self.frame += 1
            else:
                self.kill()
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)
