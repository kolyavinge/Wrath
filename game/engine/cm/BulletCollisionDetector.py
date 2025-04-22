from game.anx.CommonConstants import CommonConstants
from game.calc.RectPlane import RectPlane
from game.calc.Vector3 import Vector3
from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector
from game.engine.GameData import GameData
from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class BulletCollisionTarget:

    construction = 1
    person = 2


class BulletCollisionDetector:

    def __init__(self, gameData, levelSegmentItemFinder, planeCollisionDetector):
        self.gameData = gameData
        self.levelSegmentItemFinder = levelSegmentItemFinder
        self.planeCollisionDetector = planeCollisionDetector
        self.xNormal = Vector3(1, 0, 0)
        self.yNormal = Vector3(0, 1, 0)

    def getCollisionResultOrNone(self, bullet):
        return self.levelSegmentItemFinder.findItemOrNone(
            self.gameData.collisionTree,
            bullet.currentLevelSegment,
            bullet.nextLevelSegment,
            bullet.currentPosition,
            bullet.nextPosition,
            lambda segment, start, end: self.getTotalCollisionResultOrNone(bullet, segment, start, end),
        )

    def getTotalCollisionResultOrNone(self, bullet, levelSegment, startPoint, endPoint):
        collisionResult = self.getPersonCollisionResultOrNone(bullet, levelSegment, startPoint, endPoint)
        if collisionResult is not None:
            return (BulletCollisionTarget.person, collisionResult)

        collisionResult = self.getConstructionCollisionResultOrNone(levelSegment, startPoint, endPoint)
        if collisionResult is not None:
            return (BulletCollisionTarget.construction, collisionResult)

        return None

    def getConstructionCollisionResultOrNone(self, levelSegment, startPoint, endPoint):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for construction in levelSegment.allConstructions:
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, construction.plane, 0.1)
            if collisionPoint is not None:
                collisionPoint = construction.plane.getNearestPointOnFront(collisionPoint)
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    result = (collisionPoint, construction.frontNormal)
                    nearestLength = length

        return result

    def getPersonCollisionResultOrNone(self, bullet, levelSegment, startPoint, endPoint):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for person in levelSegment.allPerson:
            if person == bullet.ownerPerson:
                continue
            # check two cross planes
            border = person.currentBorder
            plane = RectPlane(self.xNormal, border.bottom.middleBottom, border.bottom.middleTop, border.top.middleBottom, border.top.middleTop)
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, plane, 0.1)
            if collisionPoint is None:
                plane = RectPlane(self.yNormal, border.bottom.middleRight, border.bottom.middleLeft, border.top.middleRight, border.top.middleLeft)
                collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, plane, 0.1)
            # check result
            if collisionPoint is not None:
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    result = person
                    nearestLength = length

        return result


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector(
        resolver.resolve(GameData),
        resolver.resolve(LevelSegmentItemFinder),
        resolver.resolve(PlaneCollisionDetector),
    )
