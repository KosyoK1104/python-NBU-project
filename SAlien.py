from Alien import Alien
import random
import Game
from Enemy import Enemy


class SAlien(Alien):
    def __init__(self, sprite, level):
        super().__init__(sprite, level)

    def move(self):
        if self.ALIEN_DIMENSIONS[0] == self.rect.x:
            self.direction = 'right'
        if self.rect.x == Game.Game.SIZE[0] - self.ALIEN_DIMENSIONS[0] * 2:
            self.direction = 'left'

        if self.direction == 'right':
            if self.rect.x + Enemy.SPEED < Game.Game.SIZE[0] - self.ALIEN_DIMENSIONS[0]:
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
            self.horizontal_movement = 60

        # increments the vertical position so that the aliens move down indefinitely
        self.rect.y += 1

        # if the aliens reach the bottom of the screen, they teleport back to the top
        # KosyoK: That's clever!
        if self.rect.y > Game.Game.SIZE[1]:
            self.rect.center = random.randint(0, Game.Game.SIZE[0]), -self.ALIEN_DIMENSIONS[1]
