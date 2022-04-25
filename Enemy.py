import pygame as pg
import random

SCREENRECT = pg.Rect(0, 0, 640, 480)


class Enemy(pg.sprite.Sprite):
    speed = 3

    def __int__(self):
        pg.sprite.Sprite.__init__(self)
        print('asd')
        self.facing = random.choice((-1, 1)) * Enemy.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self) -> None:
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1

