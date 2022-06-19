import json
import random
from Boss import Boss
from Enemy import Enemy
from exceptions.GameConstraintViolationException import GameConstraintViolationException
from SAlien import SAlien


class EnemyFactory:
    ALIEN = 1
    BOSS = 2

    @staticmethod
    def build(enemy_type, level) -> Enemy:
        alien_data = json.load(open("data/alien.json"))
        if level > 1:
            alien_level_dict = dict()
            for i in range(1, level + 1):
                alien_level_dict[i] = int(i * 10)
            alien_level = random.choices(list(alien_level_dict.keys()), weights=list(alien_level_dict.values()), k=1)[0]
        else:
            alien_level = 1
        if enemy_type == 1:
            # movement_type = random.choices() # Weigth
            return SAlien(random.choice(list(filter(lambda el: el['level'] == alien_level, alien_data['data'])))[
                              'sprite'], alien_level)
        if enemy_type == 2:
            return Boss(level)

        raise GameConstraintViolationException.invalid_enemy_type()
