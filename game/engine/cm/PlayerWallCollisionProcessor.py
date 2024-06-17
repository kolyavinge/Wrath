from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.model.level.Wall import WallOrientation


class PlayerWallCollisionProcessor:

    def __init__(self, gameData):
        self.gameData = gameData

    def processCollisions(self):
        player = self.gameData.player
        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                point = player.nextCenterPoint.getCopy()
                point.sub(wall.crossLine.startPoint)
                dotProduct = point.dotProduct(wall.frontNormal)
                if dotProduct < 0:
                    intersectPoint = Geometry.getLinesIntersectionPointOrNone(
                        wall.crossLine.startPoint.x,
                        wall.crossLine.startPoint.y,
                        wall.crossLine.endPoint.x,
                        wall.crossLine.endPoint.y,
                        player.currentCenterPoint.x,
                        player.currentCenterPoint.y,
                        player.nextCenterPoint.x,
                        player.nextCenterPoint.y,
                    )
                    if intersectPoint is not None:
                        if self.isPlayerLineContainsPoint(player, intersectPoint) and self.isCrossLineContainsPoint(wall, intersectPoint):
                            x, y = self.getPointOnCrossLine(wall, player.nextCenterPoint)
                            player.moveCenterPointTo(x, y)

    def getPointOnCrossLine(self, wall, playerNextCenterPoint):
        if wall.orientation == WallOrientation.horizontal:
            return (playerNextCenterPoint.x, wall.crossLine.startPoint.y)
        elif wall.orientation == WallOrientation.vertical:
            return (wall.crossLine.startPoint.x, playerNextCenterPoint.y)
        else:
            raise Exception()

    def isPlayerLineContainsPoint(self, player, point):
        x, y = point
        intersectDirection = Vector3(x, y, 0)
        intersectDirection.sub(player.currentCenterPoint)
        intersectDirection.z = 0
        if intersectDirection.getLength() < 0.01:
            return True

        playerDirection = player.nextCenterPoint.getCopy()
        playerDirection.sub(player.currentCenterPoint)
        playerDirection.z = 0

        return playerDirection.isParallel(intersectDirection) and intersectDirection.getLength() <= playerDirection.getLength()

    def isCrossLineContainsPoint(self, wall, point):
        x, y = point
        if wall.orientation == WallOrientation.horizontal:
            return wall.crossLine.startPoint.x <= x and x <= wall.crossLine.endPoint.x
        elif wall.orientation == WallOrientation.vertical:
            return wall.crossLine.startPoint.y <= y and y <= wall.crossLine.endPoint.y
        else:
            raise Exception()


def makePlayerWallCollisionProcessor(resolver):
    return PlayerWallCollisionProcessor(resolver.resolve(GameData))
