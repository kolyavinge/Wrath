from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.ai.common.EnemyCollisionDetector import EnemyCollisionDetector
from game.lib.Random import Random


class ObstacleAvoidanceLogic:

    def __init__(self, collisionDetector: EnemyCollisionDetector):
        self.collisionDetector = collisionDetector

    def getFrontNormalForNextStep(self, enemy, collisionTree):
        resultFrontNormal = Vector3()

        aiData = enemy.aiData
        isStraightDirectionCorrect = False
        direction = enemy.frontNormal.copy()
        direction.setLength(aiData.checkCollisionLength)
        if not self.collisionDetector.anyCollisions(enemy, direction, collisionTree):
            isStraightDirectionCorrect = True
            resultFrontNormal.add(direction)

        leftDirectionResult = Vector3()
        rightDirectionResult = Vector3()
        leftDirectionsCount = 0
        rightDirectionsCount = 0
        radians = aiData.checkCollisionRadianStep
        for _ in range(0, aiData.checkCollisionDirectionsCount):
            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)
            direction.setLength(aiData.checkCollisionLength)
            if not self.collisionDetector.anyCollisions(enemy, direction, collisionTree):
                leftDirectionResult.add(direction)
                leftDirectionsCount += 1

            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -radians)
            direction.setLength(aiData.checkCollisionLength)
            if not self.collisionDetector.anyCollisions(enemy, direction, collisionTree):
                rightDirectionResult.add(direction)
                rightDirectionsCount += 1

            radians += aiData.checkCollisionRadianStep

        if isStraightDirectionCorrect:
            resultFrontNormal.add(leftDirectionResult)
            resultFrontNormal.add(rightDirectionResult)
        elif leftDirectionsCount > rightDirectionsCount:
            resultFrontNormal.add(leftDirectionResult)
        elif leftDirectionsCount < rightDirectionsCount:
            resultFrontNormal.add(rightDirectionResult)
        else:  # leftDirectionsCount == rightDirectionsCount
            if Random.getBool():
                resultFrontNormal.add(leftDirectionResult)
            else:
                resultFrontNormal.add(rightDirectionResult)

        if not resultFrontNormal.isZero():
            resultFrontNormal.normalize()

        return resultFrontNormal
