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

    # create a function to move the player
    # the function will take the player's current position and the event of the key pressed
    # the key could be w, a, s, d, or the arrow keys , and the player will move in that direction
    def move(self, keys):
        self.rect.x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * self.speed
        self.rect.y += (keys[pg.K_DOWN] - keys[pg.K_UP]) * self.speed

    def attack(self, event):
        print("Player attacked")
