from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry


class PlasmaBulletMovingLogic:

    def apply(self, bullet):
        if bullet.targetPerson is not None:
            self.applyMovingLogic(bullet)
        else:
            self.findTargetPerson(bullet)
            if bullet.targetPerson is not None:
                self.applyMovingLogic(bullet)

    def applyMovingLogic(self, bullet):
        targetPersonDirection = bullet.currentPosition.getDirectionTo(bullet.targetPerson.chestCenterPoint)
        normal = bullet.velocity.copy()
        normal.vectorProduct(targetPersonDirection)
        normal.normalize()
        bullet.velocity = Geometry.rotatePoint(bullet.velocity, normal, CommonConstants.axisOrigin, bullet.homingRadians)

    def findTargetPerson(self, bullet):
        targetPersonDistance = CommonConstants.maxLevelSize
        for person in bullet.currentLevelSegment.allPerson:
            if person == bullet.ownerPerson:
                continue

            personDirection = bullet.currentPosition.getDirectionTo(person.chestCenterPoint)
            dotProduct = bullet.velocity.dotProduct(personDirection)
            if dotProduct < 0:
                continue

            personDistance = personDirection.getLength()
            if personDistance > bullet.homingDistance:
                continue

            angleBetweenCos = dotProduct / (bullet.velocityValue * personDistance)
            if angleBetweenCos < bullet.homingFieldViewRadiansCos:
                continue

            if personDistance < targetPersonDistance:
                bullet.targetPerson = person
                targetPersonDistance = personDistance


def makePlasmaBulletMovingLogic(resolver):
    return PlasmaBulletMovingLogic()
