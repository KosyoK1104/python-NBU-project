import pygame as pg
import time
import Game
import Bullet


class Player(pg.sprite.Sprite):
    DAMAGE = 30
    SPEED = 5
    MAX_HEALTH = 100
    BULLET_SPEED = 10
    print("Player class loaded")
    PLAYER_DIMENSIONS = Width, Height = 80, 80

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/player.png")
        self.image = pg.transform.scale(self.image, (Player.PLAYER_DIMENSIONS[0], Player.PLAYER_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 500
        self.health = 100
        self.attack = Player.DAMAGE
        self.speed = Player.SPEED
        self.kill_count = 0

    # create a function to move the player
    # the function will take the player's current position and the event of the key pressed
    # the key could be w, a, s, d, or the arrow keys , and the player will move in that direction
    def event_handler(self, keys):
        tmp_x = ((keys[pg.K_RIGHT] or keys[pg.K_d]) - (keys[pg.K_LEFT] or keys[pg.K_a])) * self.speed
        if 0 < self.rect.x + tmp_x < Game.Game.SIZE[0]-Player.PLAYER_DIMENSIONS[0]:
            self.rect.x += tmp_x

        tmp_y = ((keys[pg.K_DOWN] or keys[pg.K_s]) - (keys[pg.K_UP] or keys[pg.K_w])) * self.speed
        if 0 < self.rect.y + tmp_y < Game.Game.SIZE[1]-Player.PLAYER_DIMENSIONS[1]:
            self.rect.y += tmp_y

    def shoot(self) -> Bullet.Bullet:
        # print("Bullet shot")
        # create a bullet object with name bullet
        return Bullet.Bullet(self.rect.x + 15, self.rect.y, self.BULLET_SPEED)

    def draw(self, screen):
        screen.blit(self.image, self.rect)