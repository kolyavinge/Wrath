from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.AIData import EnemyState


class IdleStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        personTurnLogic: PersonTurnLogic,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.personTurnLogic = personTurnLogic

    def init(self, gameState, enemy):
        enemy.aiData.idleTimeLimit.set(Random.getInt(100, 400))
        enemy.aiData.turnTimeLimit.set(Random.getInt(50, 200))

    def process(self, gameState, enemy, inputData):
        enemy.aiData.healthPowerupDelay.decrease()
        enemy.aiData.weaponPowerupDelay.decrease()

        if self.movingLogic.isTurnTimeLimited(enemy):
            self.personTurnLogic.orientToFrontNormal(enemy, Vector3.getRandomNormalVector())

    def getNewStateOrNone(self, gameState, enemy, enemyItems):
        if enemy.aiData.stateTime > enemy.aiData.idleTimeLimit.value:
            return EnemyState.patrolling

        if enemy.health < enemy.aiData.criticalHealth and enemy.aiData.healthPowerupDelay.isExpired():
            return EnemyState.healthSearch

        if enemyItems.hasWeapons():
            otherEnemy = self.fireLogic.getEnemyWithinFireDistanceWhoFiringTo(enemy, gameState.collisionData)
            if otherEnemy is not None:
                enemy.aiData.targetPerson = otherEnemy
                return EnemyState.attack

        if enemyItems.hasWeapons() and self.fireLogic.targetExists(enemy, gameState.allPerson):
            return EnemyState.attack

        if not enemyItems.hasWeapons() and enemy.aiData.weaponPowerupDelay.isExpired():
            return EnemyState.weaponSearch

        return None
