from game.engine.ai.common.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.PersonTurnLogic import PersonTurnLogic


class MovingLogic:

    def __init__(self, personTurnLogic, obstacleAvoidanceLogic):
        self.personTurnLogic = personTurnLogic
        self.obstacleAvoidanceLogic = obstacleAvoidanceLogic

    def orientToNextDirection(self, enemy):
        nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
        if nextFrontNormal.isZero():
            nextFrontNormal = enemy.frontNormal.copy()
            nextFrontNormal.mul(-1)
        if not enemy.frontNormal.isParallel(nextFrontNormal):
            self.personTurnLogic.orientToFrontNormal(enemy, nextFrontNormal)


def makeMovingLogic(resolver):
    return MovingLogic(resolver.resolve(PersonTurnLogic), resolver.resolve(ObstacleAvoidanceLogic))
