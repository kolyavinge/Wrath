from game.engine.ai.FireLogic import FireLogic
from game.engine.ai.MovingLogic import MovingLogic
from game.model.person.Enemy import EnemyState


class WeaponSearchState:

    def __init__(self, movingLogic, fireLogic):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        pass

    def getNewStateOrNone(self, enemy):
        return None


def makeWeaponSearchState(resolver):
    return WeaponSearchState(resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
