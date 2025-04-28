from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.cm.WallCollisionDetector import WallCollisionDetector
from game.engine.GameData import GameData
from game.lib.Random import Random


class ObstacleAvoidanceLogic:

    def __init__(self, gameData, wallCollisionDetector, personCollisionDetector, traversal):
        self.gameData = gameData
        self.wallCollisionDetector = wallCollisionDetector
        self.personCollisionDetector = personCollisionDetector
        self.traversal = traversal
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
        if self.isDirectionCorrect(enemy, direction):
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
            if self.isDirectionCorrect(enemy, direction):
                leftDirectionResult.add(direction)
                leftDirectionsCount += 1

            direction = Geometry.rotatePoint(enemy.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -radians)
            direction.setLength(self.viewDepth)
            if self.isDirectionCorrect(enemy, direction):
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

    def isDirectionCorrect(self, enemy, direction):
        nextCenterPoint = enemy.currentCenterPoint.copy()
        nextCenterPoint.add(direction)
        nextCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, nextCenterPoint)

        return (
            not self.anyWallCollisions(enemy, nextCenterPoint, nextCenterPointLevelSegment)
            and not self.anyOtherPersonCollisions(enemy, nextCenterPoint, nextCenterPointLevelSegment)
            and not self.anyVoidCollisions(nextCenterPointLevelSegment)
        )

    def anyWallCollisions(self, enemy, nextCenterPoint, nextCenterPointLevelSegment):
        for wall in enemy.currentCenterPointLevelSegment.walls:
            if self.wallCollisionDetector.lineIntersectsWall(enemy.currentCenterPoint, nextCenterPoint, wall):
                return True

        if enemy.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for wall in nextCenterPointLevelSegment.walls:
                if self.wallCollisionDetector.lineIntersectsWall(enemy.currentCenterPoint, nextCenterPoint, wall):
                    return True

        return False

    def anyOtherPersonCollisions(self, enemy, nextCenterPoint, nextCenterPointLevelSegment):
        for person in enemy.currentCenterPointLevelSegment.allPerson:
            if person != enemy:
                if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                    return True

        if enemy.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for person in nextCenterPointLevelSegment.allPerson:
                if person != enemy:
                    if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                        return True

        return False

    def anyVoidCollisions(self, nextCenterPointLevelSegment):
        return len(nextCenterPointLevelSegment.floors) == 0


def makeObstacleAvoidanceLogic(resolver):
    return ObstacleAvoidanceLogic(
        resolver.resolve(GameData),
        resolver.resolve(WallCollisionDetector),
        resolver.resolve(PersonCollisionDetector),
        resolver.resolve(BSPTreeTraversal),
    )
