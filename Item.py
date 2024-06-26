import pygame as pg

import Game
from exceptions.ImageNotLoaded import ImageNotLoadedException


class Item(pg.sprite.Sprite):
    ITEM_DIMENSIONS = Width, Height = 40, 40
    SPAWN_ODDS = 200

    def __init__(self, enemy_x, enemy_y, sprite, base_damage, bullet_speed, level, time_counter):
        try:
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load(sprite)
            self.image = pg.transform.scale(self.image, (Item.ITEM_DIMENSIONS[0], Item.ITEM_DIMENSIONS[1]))
            self.rect = self.image.get_rect()
            self.rect.x = enemy_x
            self.rect.y = enemy_y
            self.time_counter = time_counter
            self.level = level
            self.base_damage = base_damage
            self.bullet_speed = bullet_speed
        except pg.error:
            raise ImageNotLoadedException.image_not_loaded(self.__class__.__name__)

    def move(self):
        self.rect.y += 1
        if self.rect.y is Game.Game.SIZE[1]:
            self.kill()

    def decrease(self):
        if self.time_counter != -1:
            self.time_counter -= 1

        if self.time_counter == 0:
            self.kill()
            return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_damage(self) -> int:
        return self.base_damage * self.level
