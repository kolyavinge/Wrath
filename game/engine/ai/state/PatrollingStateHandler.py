from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameData import GameData
from game.model.ai.AIData import EnemyState


class PatrollingStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        self.movingLogic.orientToNextDirection(enemy)
        inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if enemy in self.gameData.collisionData.personBullet:
            bullet = self.gameData.collisionData.personBullet[enemy]
            if self.fireLogic.withinFireDistance(enemy, bullet.ownerPerson):
                enemy.aiData.targetPerson = bullet.ownerPerson
                return EnemyState.attack

        if self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        return None
