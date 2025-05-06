from game.engine.ai.FireLogic import FireLogic
from game.engine.ai.MovingLogic import MovingLogic
from game.model.person.Enemy import EnemyState


class HealthSearchStateHandler:

    def __init__(self, movingLogic, fireLogic):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        pass

    def getNewStateOrNone(self, enemy):
        return None


def makeHealthSearchStateHandler(resolver):
    return HealthSearchStateHandler(resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
