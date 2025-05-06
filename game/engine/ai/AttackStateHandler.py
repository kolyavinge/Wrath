from game.engine.ai.FireLogic import FireLogic
from game.engine.ai.MovingLogic import MovingLogic
from game.model.person.Enemy import EnemyState


class AttackStateHandler:

    def __init__(self, movingLogic, fireLogic):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        self.fireLogic.orientToTargetPerson(enemy)
        inputData.fire = self.fireLogic.fire(enemy)

    def getNewStateOrNone(self, enemy):
        if not self.fireLogic.targetExists(enemy):
            return EnemyState.patrolling

        return None


def makeAttackStateHandler(resolver):
    return AttackStateHandler(resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
