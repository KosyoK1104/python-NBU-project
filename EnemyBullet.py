import pygame as pg

import Game
from Bullet import Bullet


class EnemyBullet(Bullet):
    def __init__(self, sprite, bullet_speed):
        super().__init__(sprite, bullet_speed)
        super().rotate_image(-90)

    def update(self):
        self.rect.y += self.BULLET_SPEED
        if self.rect.y > Game.Game.SIZE[1]:
            self.kill()
