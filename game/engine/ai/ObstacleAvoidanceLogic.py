from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.WallCollisionDetector import WallCollisionDetector
from game.engine.GameData import GameData


class ObstacleAvoidanceLogic:

    def __init__(self, gameData, wallCollisionDetector, traversal):
        self.gameData = gameData
        self.wallCollisionDetector = wallCollisionDetector
        self.traversal = traversal
        self.fieldViewRadians = Geometry.degreesToRadians(45.0)
        self.viewDepth = 3.0
        self.directionsCount = 8
        self.radianStep = self.fieldViewRadians / self.directionsCount

    def getFrontNormalForNextStep(self, enemy):
        resultFrontNormal = Vector3()

        direction = enemy.frontNormal.copy()
        direction.setLength(self.viewDepth)
        if self.isDirectionCorrect(enemy, direction):
            resultFrontNormal.add(direction)

        radians = self.radianStep
        for _ in range(0, self.directionsCount):
            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)
            direction.setLength(self.viewDepth)
            if self.isDirectionCorrect(enemy, direction):
                resultFrontNormal.add(direction)

            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -radians)
            direction.setLength(self.viewDepth)
            if self.isDirectionCorrect(enemy, direction):
                resultFrontNormal.add(direction)

            radians += self.radianStep

        resultFrontNormal.normalize()

        return resultFrontNormal

    def isDirectionCorrect(self, enemy, direction):
        nextCenterPoint = enemy.currentCenterPoint.copy()
        nextCenterPoint.add(direction)

        for wall in enemy.currentCenterPointLevelSegment.walls:
            if self.wallCollisionDetector.lineIntersectsWall(enemy.currentCenterPoint, nextCenterPoint, wall):
                return False

        nextCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, nextCenterPoint)
        if enemy.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for wall in nextCenterPointLevelSegment.walls:
                if self.wallCollisionDetector.lineIntersectsWall(enemy.currentCenterPoint, nextCenterPoint, wall):
                    return False

        return True


def makeObstacleAvoidanceLogic(resolver):
    return ObstacleAvoidanceLogic(resolver.resolve(GameData), resolver.resolve(WallCollisionDetector), resolver.resolve(BSPTreeTraversal))
