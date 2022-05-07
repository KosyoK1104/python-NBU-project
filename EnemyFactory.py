import json
import random

from Alien import Alien
from Boss import Boss
from Enemy import Enemy
from GameConstraintViolationException import GameConstraintViolationException


class EnemyFactory:
    # generate enemy from json file?
    ALIEN = 1
    BOSS = 2

    @staticmethod
    def build(enemy_type, level) -> Enemy:
        alien_data = json.load(open("data/alien.json"))
        if level > 1:
            alien_level_dict = dict()
            for i in range(1, level+1):
                alien_level_dict[i] = int(i * 10)
            alien_level = random.choices(list(alien_level_dict.keys()), weights=list(alien_level_dict.values()), k=1)[0]
        else:
            alien_level = 1
        if enemy_type == 1:
            return Alien(random.choice(alien_data['data'][str(alien_level)])['sprite'], alien_level)
        if enemy_type == 2:
            return Boss(level)

        raise GameConstraintViolationException.invalid_enemy_type()
