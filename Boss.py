import random

import pygame as pg

import Game
from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
from exceptions.ImageNotLoaded import ImageNotLoadedException


class Boss(Enemy):
    BOSS_DIMENSIONS = Width, Height = 200, 150
    BOSS_HEALTH = 100

    def __init__(self, level):
        try:
            Enemy.__init__(self)
            self.image = pg.image.load('data/sprites/boss.gif')
            self.image = pg.transform.scale(self.image, (self.BOSS_DIMENSIONS[0], self.BOSS_DIMENSIONS[1]))
            self.rect = self.image.get_rect()
            self.rect.x = Game.Game.SIZE[0] / 2
            self.rect.y = 0
            self.horizontal_movement = 10
            self.direction = random.choice(['left', 'right'])
            self.health = Boss.BOSS_HEALTH * (pow(2, level))
            self.attack_damage = level*2
            Game.Game.isBossAlive = True
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

        # print("Boss level {} health: ".format(level) + str(self.health))


    def move(self):
        if self.BOSS_DIMENSIONS[0] == self.rect.x:
            self.direction = 'right'
        if self.rect.x == Game.Game.SIZE[0] - self.BOSS_DIMENSIONS[0] * 2:
            self.direction = 'left'

        if self.direction == 'right':
            if self.rect.x + Enemy.SPEED < Game.Game.SIZE[0] - self.BOSS_DIMENSIONS[0]:
                self.rect.x += Enemy.SPEED
            else:
                self.direction = 'left'

        if self.direction == 'left':
            if self.rect.x - Enemy.SPEED > 0 + 10:
                self.rect.x -= Enemy.SPEED
            else:
                self.direction = 'right'

        self.horizontal_movement -= 1

        if self.horizontal_movement == 0:
            self.direction = random.choice(['left', 'right'])
            self.horizontal_movement = 30

    def kill(self) -> None:
        pg.sprite.Sprite.kill(self)
        Game.Game.isBossAlive = False

    def get_width(self):
        return self.BOSS_DIMENSIONS[0]

    def get_height(self):
        return self.BOSS_DIMENSIONS[1]

    def shoot(self) -> Bullet:
        return EnemyBullet(self, Bullet.BULLET_SPEED)
