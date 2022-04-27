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
    def move(self, event):
        if event.key == pg.K_w or event.key == pg.K_UP:
            self.rect.y -= self.speed
        if event.key == pg.K_s or event.key == pg.K_DOWN:
            self.rect.y += self.speed
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.rect.x -= self.speed
        if event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.rect.x += self.speed

    def attack(self, event):
        print("Player attacked")
