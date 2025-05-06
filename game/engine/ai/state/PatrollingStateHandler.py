from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.model.person.Enemy import EnemyState


class PatrollingStateHandler:

    def __init__(self, movingLogic, fireLogic):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        self.movingLogic.orientToNextDirection(enemy)
        inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        return None


def makePatrollingStateHandler(resolver):
    return PatrollingStateHandler(resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
