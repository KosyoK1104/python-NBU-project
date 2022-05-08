import pygame as pg

import Bullet
import Game
import Item
from typing import List


class Player(pg.sprite.Sprite):
    DAMAGE = 10
    MAX_DAMAGE = DAMAGE * (2 ^ 10)
    SPEED = 5
    MAX_HEALTH = 100
    BULLET_SPEED = 10
    PLAYER_DIMENSIONS = Width, Height = 60, 60

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/player.png")
        self.image = pg.transform.scale(self.image, (Player.PLAYER_DIMENSIONS[0], Player.PLAYER_DIMENSIONS[1]))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 500
        self.health = 10
        self.attack_damage = Player.DAMAGE
        self.speed = Player.SPEED
        self.kill_count = 0
        self.item_list: List[Item.Item] = list()

    # create a function to move the player
    # the function will take the player's current position and the event of the key pressed
    # the key could be w, a, s, d, or the arrow keys , and the player will move in that direction
    def event_handler(self, keys):
        tmp_x = ((keys[pg.K_RIGHT] or keys[pg.K_d]) - (keys[pg.K_LEFT] or keys[pg.K_a])) * self.speed
        if 0 < self.rect.x + tmp_x < Game.Game.SIZE[0] - Player.PLAYER_DIMENSIONS[0]:
            self.rect.x += tmp_x

        tmp_y = ((keys[pg.K_DOWN] or keys[pg.K_s]) - (keys[pg.K_UP] or keys[pg.K_w])) * self.speed
        if 0 < self.rect.y + tmp_y < Game.Game.SIZE[1] - Player.PLAYER_DIMENSIONS[1]:
            self.rect.y += tmp_y

    def shoot(self) -> Bullet.Bullet:
        # print("Bullet shot")
        # create a bullet object with name bullet
        return Bullet.Bullet(self, self.BULLET_SPEED)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_kill_count(self, kill_count):
        self.kill_count = kill_count

    def get_kill_count(self) -> int:
        return self.kill_count

    def add_item(self, item: Item.Item):
        self.item_list.append(item)
        self.attack_damage += item.get_damage()
        if self.attack_damage <= 0:
            self.attack_damage = 1
        self.BULLET_SPEED += item.bullet_speed

    def update_item_list(self):
        for item in self.item_list:
            if item.decrease():
                self.attack_damage -= item.get_damage()
                self.BULLET_SPEED -= item.bullet_speed
                if self.attack_damage <= 1:
                    self.attack_damage = self.DAMAGE
                self.item_list.remove(item)
