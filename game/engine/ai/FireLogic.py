from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic


class FireLogic:

    def __init__(self, gameData, personTurnLogic):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic

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
        otherEnemyDirectionLength = otherEnemyDirection.getLength()

        if otherEnemyDirectionLength > enemy.aiData.lengthForFire:
            return False

        dotProduct = enemy.frontNormal.dotProduct(otherEnemyDirection) / otherEnemyDirectionLength
        if dotProduct < enemy.aiData.horizontalFieldViewHalfCos:
            return False

        return True

    def orientToTargetPerson(self, enemy):
        frontNormal = enemy.currentCenterPoint.getDirectionTo(enemy.aiData.targetPerson.currentCenterPoint).getNormalized()
        self.personTurnLogic.orientToFrontNormal(enemy, frontNormal)


def makeFireLogic(resolver):
    return FireLogic(resolver.resolve(GameData), resolver.resolve(PersonTurnLogic))
