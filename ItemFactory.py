import json
import random

from Enemy import Enemy
from Item import Item


class ItemFactory:
    @staticmethod
    def build(level, enemy: Enemy):
        items_json = json.load(open("data/items.json"))
        items = items_json['data']
        item = random.choice(items)
        return Item(
            enemy.rect.x,
            enemy.rect.y,
            item['sprite'],
            item['base_damage'],
            item['bullet_speed'],
            level,
            item['item_cooldown']
        )
