from game.anx.PersonConstants import PersonConstants
from game.engine.ai.BurstFireLogic import BurstFireLogic
from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic


class FireLogic:

    def __init__(self, gameData, personTurnLogic, burstFireLogic):
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
        otherEnemyDirection = enemy.currentCenterPoint.getDirectionTo(otherEnemy.currentCenterPoint)
        otherEnemyDistance = otherEnemyDirection.getLength()

        if otherEnemyDistance > enemy.aiData.fireDistance:
            return False

        dotProduct = enemy.frontNormal.dotProduct(otherEnemyDirection) / otherEnemyDistance
        if dotProduct < enemy.aiData.horizontalFieldViewHalfCos:
            return False

        return True

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

    def fire(self, enemy):
        enemyItems = self.gameData.allPersonItems[enemy]
        if enemyItems.currentWeapon.isBurstModeEnabled:
            return self.burstFireLogic.fire(enemy, enemyItems)
        else:
            return True


def makeFireLogic(resolver):
    return FireLogic(resolver.resolve(GameData), resolver.resolve(PersonTurnLogic), resolver.resolve(BurstFireLogic))
