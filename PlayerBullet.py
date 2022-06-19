import pygame as pg

from Bullet import Bullet


class PlayerBullet(Bullet):
    def __init__(self, sprite, bullet_speed):
        super().__init__(sprite, bullet_speed)
        super().rotate_image(90)

    def update(self):
        self.rect.y -= self.BULLET_SPEED
        if self.rect.y < 0:
            self.kill()


