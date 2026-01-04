from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameState import GameState
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.AIData import EnemyState


class IdleStateHandler:

    def __init__(
        self,
        gameData: GameState,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.personTurnLogic = personTurnLogic

    def init(self, enemy):
        enemy.aiData.idleTimeLimit.set(Random.getInt(100, 400))
        enemy.aiData.turnTimeLimit.set(Random.getInt(50, 200))

    def process(self, enemy, inputData):
        enemy.aiData.healthPowerupDelay.decrease()
        enemy.aiData.weaponPowerupDelay.decrease()

        if self.movingLogic.isTurnTimeLimited(enemy):
            self.personTurnLogic.orientToFrontNormal(enemy, Vector3.getRandomNormalVector())

    def getNewStateOrNone(self, enemy):
        if enemy.aiData.stateTime > enemy.aiData.idleTimeLimit.value:
            return EnemyState.patrolling

        if enemy.health < enemy.aiData.criticalHealth and enemy.aiData.healthPowerupDelay.isExpired():
            return EnemyState.healthSearch

        enemyItems = self.gameData.enemyItems[enemy]

        if enemyItems.hasWeapons():
            otherEnemy = self.fireLogic.getEnemyWithinFireDistanceWhoFiringTo(enemy)
            if otherEnemy is not None:
                enemy.aiData.targetPerson = otherEnemy
                return EnemyState.attack

        if enemyItems.hasWeapons() and self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        if not enemyItems.hasWeapons() and enemy.aiData.weaponPowerupDelay.isExpired():
            return EnemyState.weaponSearch

        return None
