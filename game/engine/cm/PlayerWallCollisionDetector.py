from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Numeric import Numeric
from game.model.Orientation import Orientation


class PlayerWallCollisionDetector:

    def __init__(self, gameData):
        self.gameData = gameData

    def getCollidedWalls(self):
        player = self.gameData.player
        if not player.hasMoved:
            return []

        collidedWalls = []

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.horizontalVerticalWalls:
                if self.hasCollision(player, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.diagonalWalls:
                if self.hasCollision(player, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        return collidedWalls

    def hasCollision(self, player, wall):
        currentBorder = player.currentBorder.bottom
        nextBorder = player.nextBorder.bottom
        # check corners
        result = self.playerLineIntersectsWall(currentBorder.downLeft, nextBorder.downLeft, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.downRight, nextBorder.downRight, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.upLeft, nextBorder.upLeft, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.upRight, nextBorder.upRight, wall)
        # check middle
        result = result or self.playerLineIntersectsWall(currentBorder.middleLeft, nextBorder.middleLeft, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.middleRight, nextBorder.middleRight, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.middleTop, nextBorder.middleTop, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.middleBottom, nextBorder.middleBottom, wall)

        return result

    def playerLineIntersectsWall(self, playerPointFrom, playerPointTo, wall):
        if self.isPlayerPointBehindWall(playerPointTo, wall):
            intersectPoint = self.getWallIntersectPointOrNone(playerPointFrom, playerPointTo, wall)
            if intersectPoint is not None:
                if self.playerLineContainsPoint(playerPointFrom, playerPointTo, intersectPoint) and self.wallContainsPoint(wall, intersectPoint):
                    return True

        return False

    def isPlayerPointBehindWall(self, playerPoint, wall):
        behindDirection = wall.startPoint.getDirectionTo(playerPoint)
        dotProduct = behindDirection.dotProduct(wall.frontNormal)

        return dotProduct < 0

    def getWallIntersectPointOrNone(self, playerPointFrom, playerPointTo, wall):
        return Geometry.getLinesIntersectPointOrNone(
            wall.startPoint.x,
            wall.startPoint.y,
            wall.endPoint.x,
            wall.endPoint.y,
            playerPointFrom.x,
            playerPointFrom.y,
            playerPointTo.x,
            playerPointTo.y,
        )

    def playerLineContainsPoint(self, playerPointFrom, playerPointTo, point):
        x, y = point
        return Geometry.lineContainsPoint(playerPointFrom.x, playerPointFrom.y, playerPointTo.x, playerPointTo.y, x, y)

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


def makePlayerWallCollisionDetector(resolver):
    return PlayerWallCollisionDetector(resolver.resolve(GameData))
