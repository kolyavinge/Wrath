from game.engine.ai.FireLogic import FireLogic
from game.engine.ai.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic


class EnemyAILogic:

    def __init__(self, gameData, personTurnLogic, obstacleAvoidanceLogic, fireLogic):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic
        self.obstacleAvoidanceLogic = obstacleAvoidanceLogic
        self.fireLogic = fireLogic

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            self.applyForEnemy(enemy, inputData)

    def applyForEnemy(self, enemy, inputData):
        inputData.clear()

        if self.fireLogic.targetExists(enemy):
            self.fireLogic.orientToTargetPerson(enemy)
            inputData.fire = True
        else:
            nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
            if nextFrontNormal.isZero():
                nextFrontNormal = enemy.frontNormal.copy()
                nextFrontNormal.mul(-1)
            if not enemy.frontNormal.isParallel(nextFrontNormal):
                self.personTurnLogic.orientByFrontNormal(enemy, nextFrontNormal)
            inputData.goForward = True


def makeEnemyAILogic(resolver):
    return EnemyAILogic(
        resolver.resolve(GameData), resolver.resolve(PersonTurnLogic), resolver.resolve(ObstacleAvoidanceLogic), resolver.resolve(FireLogic)
    )
