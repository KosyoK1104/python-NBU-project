import pygame as pg


# create a bullet class with a constructor
from exceptions.ImageNotLoaded import ImageNotLoadedException


class Bullet(pg.sprite.Sprite):
    BULLET_DIMENSIONS = (50, 50)
    BULLET_SPEED = 10

    def __init__(self, player, bullet_speed):
        try:
            pg.sprite.Sprite.__init__(self)
            self.BULLET_SPEED = bullet_speed
            self.damage = player.attack_damage
            self.image = pg.image.load("data/sprites/lasers/{}.png".format((self.damage // 20)+10))
            self.image = pg.transform.scale(self.image, (Bullet.BULLET_DIMENSIONS[0], Bullet.BULLET_DIMENSIONS[1]))
            self.image = pg.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
            self.rect.center = (player.rect.centerx, player.rect.centery-20)
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

    def get_damage(self) -> int:
        return self.damage

    def update(self):
        self.rect.y -= self.BULLET_SPEED
        if self.rect.y < 0:
            self.kill()

    def kill(self) -> None:
        pg.sprite.Sprite.kill(self)





