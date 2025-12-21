from game.anx.PersonConstants import PersonConstants
from game.engine.ai.common.BurstFireLogic import BurstFireLogic
from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.model.person.PersonStates import LifeCycle


class FireLogic:

    def __init__(
        self,
        gameData: GameData,
        personTurnLogic: PersonTurnLogic,
        burstFireLogic: BurstFireLogic,
    ):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic
        self.burstFireLogic = burstFireLogic

    def targetExists(self, enemy):
        return self.isCurrentTargetAvailable(enemy) or self.isNewTargetFound(enemy)

    def isCurrentTargetAvailable(self, enemy):
        if enemy.aiData.targetPerson is None:
            return False

        if not self.canFireToOtherEnemy(enemy, enemy.aiData.targetPerson):
            enemy.aiData.targetPerson = None
            return False

        return True

    def isNewTargetFound(self, enemy):
        enemy.aiData.targetPerson = None
        for otherEnemy in self.gameData.allPerson:
            if enemy != otherEnemy and self.canFireToOtherEnemy(enemy, otherEnemy):
                enemy.aiData.targetPerson = otherEnemy
                return True

        return False

    def canFireToOtherEnemy(self, enemy, otherEnemy):
        if otherEnemy.lifeCycle != LifeCycle.alive:
            return False

        otherEnemyDirection = enemy.currentCenterPoint.getDirectionTo(otherEnemy.currentCenterPoint)
        otherEnemyDistance = otherEnemyDirection.getLength()

        if otherEnemyDistance > enemy.aiData.fireDistance:
            return False

        dotProduct = enemy.frontNormal.dotProduct(otherEnemyDirection) / otherEnemyDistance
        if dotProduct < enemy.aiData.horizontalFieldViewHalfCos:
            return False

        return True

    def withinFireDistance(self, enemy, otherEnemy):
        return enemy.currentCenterPoint.getLengthTo(otherEnemy.currentCenterPoint) < enemy.aiData.fireDistance

    def orientToTargetPerson(self, enemy):
        targetPerson = enemy.aiData.targetPerson
        if targetPerson.velocityValue > 0:  # цель двигается - целится на опережение
            targetPersonPosition = targetPerson.velocityVector.copy()
            targetPersonPosition.setLength(PersonConstants.xyLengthHalf)
            targetPersonPosition.add(targetPerson.currentCenterPoint)
        else:
            targetPersonPosition = targetPerson.currentCenterPoint
        frontNormal = enemy.currentCenterPoint.getDirectionTo(targetPersonPosition).getNormalized()
        self.personTurnLogic.orientToFrontNormal(enemy, frontNormal)

    def getEnemyWithinFireDistanceWhoFiringTo(self, enemy):
        if enemy in self.gameData.collisionData.personBullet:
            bullet = self.gameData.collisionData.personBullet[enemy]
            if bullet.ownerPerson is not None and self.withinFireDistance(enemy, bullet.ownerPerson):
                return bullet.ownerPerson

        return None

    def applyInputData(self, enemy, inputData):
        enemyItems = self.gameData.allPersonItems[enemy]
        if enemyItems.currentWeapon.isBurstModeEnabled:
            inputData.fire = self.burstFireLogic.fire(enemy, enemyItems)
        else:
            inputData.fire = True
