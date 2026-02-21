from game.anx.PersonConstants import PersonConstants
from game.engine.ai.common.BurstFireLogic import BurstFireLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.model.person.PersonStates import LifeCycle


class FireLogic:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        burstFireLogic: BurstFireLogic,
    ):
        self.personTurnLogic = personTurnLogic
        self.burstFireLogic = burstFireLogic

    def targetExists(self, bot, allPerson):
        return self.isCurrentTargetAvailable(bot) or self.isNewTargetFound(bot, allPerson)

    def isCurrentTargetAvailable(self, bot):
        if bot.aiData.targetPerson is None:
            return False

        if not self.canFireToOtherEnemy(bot, bot.aiData.targetPerson):
            bot.aiData.targetPerson = None
            return False

        return True

    def isNewTargetFound(self, bot, allPerson):
        bot.aiData.targetPerson = None
        for otherEnemy in allPerson:
            if bot != otherEnemy and self.canFireToOtherEnemy(bot, otherEnemy):
                bot.aiData.targetPerson = otherEnemy
                return True

        return False

    def canFireToOtherEnemy(self, bot, otherEnemy):
        if otherEnemy.lifeCycle != LifeCycle.alive:
            return False

        otherEnemyDirection = bot.currentCenterPoint.getDirectionTo(otherEnemy.currentCenterPoint)
        otherEnemyDistance = otherEnemyDirection.getLength()

        if otherEnemyDistance > bot.aiData.fireDistance:
            return False

        dotProduct = bot.frontNormal.dotProduct(otherEnemyDirection) / otherEnemyDistance
        if dotProduct < bot.aiData.horizontalFieldViewHalfCos:
            return False

        return True

    def withinFireDistance(self, bot, otherEnemy):
        return bot.currentCenterPoint.getLengthTo(otherEnemy.currentCenterPoint) < bot.aiData.fireDistance

    def orientToTargetPerson(self, bot):
        targetPerson = bot.aiData.targetPerson
        if targetPerson.velocityValue > 0:  # цель двигается - целится на опережение
            targetPersonPosition = targetPerson.velocityVector.copy()
            targetPersonPosition.setLength(PersonConstants.xyLengthHalf)
            targetPersonPosition.add(targetPerson.currentCenterPoint)
        else:
            targetPersonPosition = targetPerson.currentCenterPoint
        frontNormal = bot.currentCenterPoint.getDirectionTo(targetPersonPosition).getNormalized()
        self.personTurnLogic.orientToFrontNormal(bot, frontNormal)

    def getEnemyWithinFireDistanceWhoFiringTo(self, bot, collisionData):
        if bot in collisionData.personBullet:
            bullet = collisionData.personBullet[bot]
            if bullet.ownerPerson is not None and self.withinFireDistance(bot, bullet.ownerPerson):
                return bullet.ownerPerson

        if bot in collisionData.personRay:
            ray = collisionData.personRay[bot]
            if self.withinFireDistance(bot, ray.ownerPerson):
                return ray.ownerPerson

        return None

    def applyInputData(self, bot, enemyItems, inputData):
        if enemyItems.currentWeapon.isBurstModeEnabled:
            inputData.fire = self.burstFireLogic.fire(bot, enemyItems)
        else:
            inputData.fire = True
