from game.calc.Geometry import Geometry
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal
        self.maxCosLookDirection = Math.cos(self.gameData.camera.viewAngleRadians)

    def updateIfPlayerMovedOrTurned(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.update()

    def update(self):
        self.gameData.visibleLevelSegments = set()
        self.checkedJoinLines = set()
        self.visibleWalls = []
        for levelSegment in self.gameData.player.visibilityLevelSegments:
            self.checkLevelSegment(levelSegment)

    def checkLevelSegment(self, levelSegment):
        self.gameData.visibleLevelSegments.add(levelSegment)
        self.visibleWalls.extend(levelSegment.checkSegmentVisibilityWalls)
        for joinLine in levelSegment.joinLines:
            if joinLine not in self.checkedJoinLines:
                self.checkedJoinLines.add(joinLine)
                if self.isJoinLineVisible(joinLine):
                    joinedLevelSegment = joinLine.backLevelSegment if joinLine.frontLevelSegment == levelSegment else joinLine.frontLevelSegment
                    self.checkLevelSegment(joinedLevelSegment)

    def isJoinLineVisible(self, joinLine):
        for point in joinLine.points:
            if self.isPointVisible(point):
                return True

        return False

    def isPointVisible(self, point):
        startPoint = self.gameData.camera.position
        endPoint = point
        direction = startPoint.getDirectionTo(endPoint)

        direction2d = direction.copy()
        direction2d.z = 0
        direction2d.normalize()

        look2d = self.gameData.camera.lookDirection.copy()
        look2d.z = 0
        look2d.normalize()

        dotProduct = look2d.dotProduct(direction2d)
        if dotProduct < self.maxCosLookDirection:
            return False

        for wall in self.visibleWalls:
            intersectPoint = Geometry.getLinesIntersectPointOrNone(
                wall.startPoint.x, wall.startPoint.y, wall.endPoint.x, wall.endPoint.y, startPoint.x, startPoint.y, endPoint.x, endPoint.y
            )
            if intersectPoint is not None:
                x, y = intersectPoint
                if Geometry.lineContainsPoint(
                    wall.startPoint.x, wall.startPoint.y, wall.endPoint.x, wall.endPoint.y, x, y
                ) and Geometry.lineContainsPoint(startPoint.x, startPoint.y, endPoint.x, endPoint.y, x, y):
                    return False

        return True


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
