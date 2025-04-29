from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.ai.CollisionDetector import CollisionDetector
from game.lib.Random import Random


class ObstacleAvoidanceLogic:

    def __init__(self, collisionDetector):
        self.collisionDetector = collisionDetector
        self.fieldViewRadians = Geometry.degreesToRadians(45.0)
        self.viewDepth = 3.0
        self.directionsCount = 8
        self.radianStep = self.fieldViewRadians / self.directionsCount
        self.rand = Random()

    def getFrontNormalForNextStep(self, enemy):
        resultFrontNormal = Vector3()

        isCurrentFrontNormalCorrect = False
        direction = enemy.frontNormal.copy()
        direction.setLength(self.viewDepth)
        if not self.collisionDetector.anyCollisions(enemy, direction):
            isCurrentFrontNormalCorrect = True
            resultFrontNormal.add(direction)

        leftDirectionResult = Vector3()
        rightDirectionResult = Vector3()
        leftDirectionsCount = 0
        rightDirectionsCount = 0
        radians = self.radianStep
        for _ in range(0, self.directionsCount):
            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)
            direction.setLength(self.viewDepth)
            if not self.collisionDetector.anyCollisions(enemy, direction):
                leftDirectionResult.add(direction)
                leftDirectionsCount += 1

            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -radians)
            direction.setLength(self.viewDepth)
            if not self.collisionDetector.anyCollisions(enemy, direction):
                rightDirectionResult.add(direction)
                rightDirectionsCount += 1

            radians += self.radianStep

        if isCurrentFrontNormalCorrect:
            resultFrontNormal.add(leftDirectionResult)
            resultFrontNormal.add(rightDirectionResult)
        elif leftDirectionsCount > rightDirectionsCount:
            resultFrontNormal.add(leftDirectionResult)
        elif leftDirectionsCount < rightDirectionsCount:
            resultFrontNormal.add(rightDirectionResult)
        else:
            if self.rand.getInt(-100, 100) % 2 == 0:
                resultFrontNormal.add(leftDirectionResult)
            else:
                resultFrontNormal.add(rightDirectionResult)

        if not resultFrontNormal.isZero():
            resultFrontNormal.normalize()

        return resultFrontNormal


def makeObstacleAvoidanceLogic(resolver):
    return ObstacleAvoidanceLogic(
        resolver.resolve(CollisionDetector),
    )
