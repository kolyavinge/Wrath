from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.model.level.Orientation import Orientation


class PlayerWallCollisionProcessor:

    def __init__(self, gameData):
        self.gameData = gameData
        self.hasCollisions = False

    def processCollisions(self):
        self.hasCollisions = False
        if self.gameData.player.hasMoved:
            for levelSegment in self.gameData.player.levelSegments:
                for wall in levelSegment.walls:
                    self.processWall(wall)

    def processWall(self, wall):
        player = self.gameData.player
        if self.isPlayerBehindWall(player, wall):
            intersectPoint = self.getCrossLineIntersectPointOrNone(player, wall)
            if intersectPoint is not None:
                if self.playerLineContainsPoint(player, intersectPoint) and self.crossLineContainsPoint(wall, intersectPoint):
                    x, y = self.getPointOnCrossLine(wall, player.nextCenterPoint)
                    player.moveNextPositionTo(Vector3(x, y, 0))
                    self.hasCollisions = True

    def isPlayerBehindWall(self, player, wall):
        point = player.nextCenterPoint.getCopy()
        point.sub(wall.crossLine.startPoint)
        dotProduct = point.dotProduct(wall.frontNormal)

        return dotProduct < 0

    def getCrossLineIntersectPointOrNone(self, player, wall):
        return Geometry.getLinesIntersectPointOrNone(
            wall.crossLine.startPoint.x,
            wall.crossLine.startPoint.y,
            wall.crossLine.endPoint.x,
            wall.crossLine.endPoint.y,
            player.currentCenterPoint.x,
            player.currentCenterPoint.y,
            player.nextCenterPoint.x,
            player.nextCenterPoint.y,
        )

    def playerLineContainsPoint(self, player, point):
        x, y = point
        return Geometry.lineContainsPoint(
            player.currentCenterPoint.x, player.currentCenterPoint.y, player.nextCenterPoint.x, player.nextCenterPoint.y, x, y
        )

    def crossLineContainsPoint(self, wall, point):
        x, y = point
        crossLine = wall.crossLine
        if wall.orientation == Orientation.horizontal:
            return crossLine.startPoint.x <= x and x <= crossLine.endPoint.x
        elif wall.orientation == Orientation.vertical:
            return crossLine.startPoint.y <= y and y <= crossLine.endPoint.y
        elif wall.orientation == Orientation.diagonalDownLeftUpRight or wall.orientation == Orientation.diagonalUpLeftDownRight:
            return Geometry.lineContainsPoint(crossLine.startPoint.x, crossLine.startPoint.y, crossLine.endPoint.x, crossLine.endPoint.y, x, y)
        else:
            raise Exception()

    def getPointOnCrossLine(self, wall, playerNextCenterPoint):
        if wall.orientation == Orientation.horizontal:
            return (playerNextCenterPoint.x, wall.crossLine.startPoint.y)
        elif wall.orientation == Orientation.vertical:
            return (wall.crossLine.startPoint.x, playerNextCenterPoint.y)
        elif wall.orientation == Orientation.diagonalDownLeftUpRight or wall.orientation == Orientation.diagonalUpLeftDownRight:
            playerDirection = playerNextCenterPoint.getCopy()
            playerDirection.sub(wall.crossLine.startPoint)
            projected = Geometry.getProjectedVector(playerDirection, wall.crossLineDirection)
            projected.add(wall.crossLine.startPoint)

            return (projected.x, projected.y)
        else:
            raise Exception()


def makePlayerWallCollisionProcessor(resolver):
    return PlayerWallCollisionProcessor(resolver.resolve(GameData))
