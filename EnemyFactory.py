import json
import random

from GameConstraintViolationException import GameConstraintViolationException
from Alien import Alien
from Boss import Boss
from Enemy import Enemy


class EnemyFactory:
    # generate enemy from json file?
    ALIEN = 1
    BOSS = 2

    @staticmethod
    def build(enemyType, level) -> Enemy:
        alien_data = json.load(open("data/alien.json"))
        # enemyType = 1
        # level = 1
        # alien_level = random.randint(1, level)
        if level > 1:
            alien_level_dict = dict()
            # loop that generates dict with key = level and value = weighted chance
            for i in range(1, level+1):
                alien_level_dict[i] = int(i * 10)
            # keys represent different levels, values represent chance of spawning
            # print(list(alien_level_dict.values()))
            # print(list(alien_level_dict.keys()))
            alien_level = random.choices(list(alien_level_dict.keys()), weights=list(alien_level_dict.values()), k=1)[0]
            # print(alien_level)
        else:
            alien_level = 1


        if enemyType == 1:
            return Alien(random.choice(alien_data['data'][str(alien_level)])['sprite'], alien_level)
        if enemyType == 2:
            return Boss(level)

        raise GameConstraintViolationException.invalid_enemy_type()
