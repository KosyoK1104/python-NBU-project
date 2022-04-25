from Alien import Alien
from Boss import Boss
from Enemy import Enemy


class EnemyFactory:
    # generate enemy from json file?
    @staticmethod
    def build(enemyType) -> Enemy:
        if enemyType == 1:
            return Alien()
        if enemyType == 2:
            return Boss()
        # throw exception?
        return Enemy()
