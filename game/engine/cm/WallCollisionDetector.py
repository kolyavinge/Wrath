from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder
from game.lib.Numeric import Numeric
from game.model.Orientation import Orientation


class WallCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        levelSegmentItemFinder: LevelSegmentItemFinder,
    ):
        self.gameData = gameData
        self.levelSegmentItemFinder = levelSegmentItemFinder

    def anyCollisions(self, linePointFrom, linePointTo, fromLevelSegment, toLevelSegment):
        return (
            self.levelSegmentItemFinder.findItemOrNone(
                self.gameData.collisionTree,
                fromLevelSegment,
                toLevelSegment,
                linePointFrom,
                linePointTo,
                lambda segment, start, end: self.checkCollisionOrNone(start, end, segment.walls),
            )
            or False
        )

    def checkCollisionOrNone(self, linePointFrom, linePointTo, walls):
        for wall in walls:
            if self.lineIntersectsWall(linePointFrom, linePointTo, wall):
                return True

        return None

    def lineIntersectsWall(self, linePointFrom, linePointTo, wall):
        if self.isLinePointToBehindWall(linePointTo, wall):
            intersectPoint = self.getWallIntersectPointOrNone(linePointFrom, linePointTo, wall)
            if intersectPoint is not None:
                if self.lineContainsPoint(linePointFrom, linePointTo, intersectPoint) and self.wallContainsPoint(wall, intersectPoint):
                    return True

        return False

    def isLinePointToBehindWall(self, linePointTo, wall):
        x = linePointTo.x - wall.startPoint.x
        y = linePointTo.y - wall.startPoint.y
        z = linePointTo.z - wall.startPoint.z
        dotProduct = wall.frontNormal.x * x + wall.frontNormal.y * y + wall.frontNormal.z * z

        return dotProduct < 0

    def getWallIntersectPointOrNone(self, linePointFrom, linePointTo, wall):
        return Geometry.getLinesIntersectPointOrNone(
            wall.startPoint.x,
            wall.startPoint.y,
            wall.endPoint.x,
            wall.endPoint.y,
            linePointFrom.x,
            linePointFrom.y,
            linePointTo.x,
            linePointTo.y,
        )

    def lineContainsPoint(self, linePointFrom, linePointTo, point):
        x, y = point
        return Geometry.lineContainsPoint(linePointFrom.x, linePointFrom.y, linePointTo.x, linePointTo.y, x, y)

    def wallContainsPoint(self, wall, point):
        x, y = point
        if wall.orientation == Orientation.horizontal:
            return Numeric.between(x, wall.startPoint.x, wall.endPoint.x) or Numeric.between(x, wall.endPoint.x, wall.startPoint.x)
        elif wall.orientation == Orientation.vertical:
            return Numeric.between(y, wall.startPoint.y, wall.endPoint.y) or Numeric.between(y, wall.endPoint.y, wall.startPoint.y)
        elif wall.orientation == Orientation.diagonal:
            return Geometry.lineContainsPoint(wall.startPoint.x, wall.startPoint.y, wall.endPoint.x, wall.endPoint.y, x, y)
        else:
            raise Exception("Wrong wall orientation.")
