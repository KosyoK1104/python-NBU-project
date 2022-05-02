import pygame as pg


class Explosion(pg.sprite.Sprite):
    EXPLOSION_DIMENSIONS = (200, 200)

    def __init__(self, object) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/Explosion/1.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (Explosion.EXPLOSION_DIMENSIONS[0], Explosion.EXPLOSION_DIMENSIONS[1]))
        self.rect = self.image.get_rect()

        # IDK why this offset is that big but it is
        self.rect.x = object.rect.x-80
        self.rect.y = object.rect.y-50
        self.frame = 1

    def update(self) -> None:
        self.image = pg.image.load("data/Explosion/{}.png".format(self.frame)).convert_alpha()
        self.image = pg.transform.scale(self.image, (Explosion.EXPLOSION_DIMENSIONS[0], Explosion.EXPLOSION_DIMENSIONS[1]))
        if self.frame < 63:
            self.frame += 1
        else:
            self.kill()

    def kill(self) -> None:
        pg.sprite.Sprite.kill(self)
