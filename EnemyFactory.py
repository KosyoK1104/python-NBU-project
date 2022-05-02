import json
import random

from GameConstraintViolationException import GameConstraintViolationException
from Alien import Alien
from Boss import Boss
from Enemy import Enemy


class EnemyFactory:
    # generate enemy from json file?
    @staticmethod
    def build(enemyType, level) -> Enemy:
        alien_data = json.load(open("data/alien.json"))
        enemyType = 3
        alien_level = random.randint(1, level)

        if enemyType == 1:
            return Alien(random.choice(alien_data['data'][str(alien_level)])['sprite'])
        if enemyType == 2:
            return Boss()

        raise GameConstraintViolationException.invalid_enemy_type()
