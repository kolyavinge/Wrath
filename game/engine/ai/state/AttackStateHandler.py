from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.model.person.Enemy import EnemyState


class AttackStateHandler:

    def __init__(self, movingLogic, fireLogic):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        self.movingLogic.updateMoveDirection(enemy)
        self.movingLogic.applyInputData(enemy, inputData)
        self.fireLogic.orientToTargetPerson(enemy)
        self.fireLogic.applyInputData(enemy, inputData)

    def getNewStateOrNone(self, enemy):
        if not self.fireLogic.targetExists(enemy):
            return EnemyState.patrolling

        return None


def makeAttackStateHandler(resolver):
    return AttackStateHandler(resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
