import pygame as pg
import Game


# create a bullet class with a constructor
class Bullet(pg.sprite.Sprite):
    BULLET_DIMENSIONS = (50, 50)
    BULLET_SPEED = 10

    def __init__(self, x, y, bullet_speed):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/Laser Sprites/11.png")
        self.image = pg.transform.scale(self.image, (Bullet.BULLET_DIMENSIONS[0], Bullet.BULLET_DIMENSIONS[1]))
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.BULLET_SPEED = bullet_speed

    def move(self):
        self.rect.y -= self.BULLET_SPEED


