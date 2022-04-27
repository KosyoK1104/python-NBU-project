import pygame as pg


class Player(pg.sprite.Sprite):
    DAMAGE = 30
    SPEED = 10
    MAX_HEALTH = 100
    print("Player class loaded")

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/player.png")
        self.image = pg.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 500
        self.health = 100
        self.attack = Player.DAMAGE
        self.speed = Player.SPEED

