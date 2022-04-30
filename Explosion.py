import pygame as pg


class Explosion(pg.sprite.Sprite):
    EXPLOSION_DIMENSIONS = (200, 200)
    def __init__(self, object):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/Explosion/1.png")
        self.image = pg.transform.scale(self.image, (Explosion.EXPLOSION_DIMENSIONS[0], Explosion.EXPLOSION_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = object.rect.x
        self.rect.y = object.rect.y
        self.frame = 1

    def update(self):
        self.image = pg.image.load("data/Explosion/{}.png".format(self.frame))
        self.image = pg.transform.scale(self.image, (Explosion.EXPLOSION_DIMENSIONS[0], Explosion.EXPLOSION_DIMENSIONS[1]))
        if self.frame < 63:
            self.frame += 1
        else:
            self.kill()

    def kill(self) -> None:
        pg.sprite.Sprite.kill(self)
