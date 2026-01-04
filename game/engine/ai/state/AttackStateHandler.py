from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameState import GameState
from game.model.ai.AIData import EnemyState


class AttackStateHandler:

    def __init__(
        self,
        gameState: GameState,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
    ):
        self.gameState = gameState
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def init(self, enemy):
        pass

    def process(self, enemy, inputData):
        enemy.aiData.healthPowerupDelay.decrease()
        enemy.aiData.weaponPowerupDelay.decrease()

        self.movingLogic.updateMoveDirection(enemy)

        if not enemy.aiData.runAwayFromObstacle and enemy in self.gameState.collisionData.personPerson:
            enemy.aiData.runAwayFromObstacle = True
            otherEnemy = self.gameState.collisionData.personPerson[enemy]
            if enemy.velocityValue > 0 and otherEnemy.velocityValue > 0:
                if not enemy.velocityVector.isParallel(otherEnemy.velocityVector, 0.1):
                    self.movingLogic.setOppositeMoveDirection(enemy)
            else:
                self.movingLogic.setOppositeMoveDirection(enemy)

        self.movingLogic.applyMoveDirectionInputData(enemy, inputData)

        self.fireLogic.orientToTargetPerson(enemy)
        self.fireLogic.applyInputData(enemy, inputData)

    def getNewStateOrNone(self, enemy):
        if enemy.health < enemy.aiData.criticalHealth and enemy.aiData.healthPowerupDelay.isExpired():
            return EnemyState.healthSearch

        if not self.fireLogic.targetExists(enemy):
            return EnemyState.patrolling

        enemyItems = self.gameState.enemyItems[enemy]

        if not enemyItems.hasWeapons() and enemy.aiData.weaponPowerupDelay.isExpired():
            return EnemyState.weaponSearch

        return None
