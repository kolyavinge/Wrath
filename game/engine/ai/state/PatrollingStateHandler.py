from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.AIData import EnemyState


class PatrollingStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.personTurnLogic = personTurnLogic

    def init(self, enemy):
        enemy.aiData.patrollingTimeLimit.set(Random.getInt(500, 2000))
        enemy.aiData.turnTimeLimit.set(Random.getInt(100, 1000))

    def process(self, enemy, inputData):
        enemy.aiData.healthPowerupDelay.decrease()
        enemy.aiData.weaponPowerupDelay.decrease()

        if self.movingLogic.isTurnTimeLimited(enemy):
            enemy.aiData.turnTimeLimit.set(Random.getInt(100, 1000))
            self.personTurnLogic.orientToFrontNormal(enemy, Vector3.getRandomNormalVector())

        self.movingLogic.orientToFreeDirection(enemy)
        inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if enemy.aiData.stateTime > enemy.aiData.patrollingTimeLimit.value:
            return EnemyState.idle

        if enemy.health < enemy.aiData.criticalHealth and enemy.aiData.healthPowerupDelay.isExpired():
            return EnemyState.healthSearch

        otherEnemy = self.fireLogic.getEnemyWithinFireDistanceWhoFiringTo(enemy)
        if otherEnemy is not None:
            enemy.aiData.targetPerson = otherEnemy
            return EnemyState.attack

        if self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        if not self.gameData.enemyItems[enemy].hasWeapons() and enemy.aiData.weaponPowerupDelay.isExpired():
            return EnemyState.weaponSearch

        return None
