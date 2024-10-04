from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.model.Orientation import Orientation


class PlayerWallCollisionDetector:

    def __init__(self, gameData):
        self.gameData = gameData

    def detectCollisions(self):
        self.gameData.playerCollidedWalls = []

        player = self.gameData.player
        if not player.hasMoved:
            return

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.horizontalVerticalWalls:
                if self.hasCollision(player, wall):
                    if wall not in self.gameData.playerCollidedWalls:
                        self.gameData.playerCollidedWalls.append(wall)

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.diagonalWalls:
                if self.hasCollision(player, wall):
                    if wall not in self.gameData.playerCollidedWalls:
                        self.gameData.playerCollidedWalls.append(wall)

    def hasCollision(self, player, wall):
        if self.playerCanStepOverWall(player, wall):
            return False

        currentBorder = player.currentBorder.bottom
        nextBorder = player.nextBorder.bottom
        result = self.playerLineIntersectsWall(currentBorder.downLeft, nextBorder.downLeft, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.downRight, nextBorder.downRight, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.upLeft, nextBorder.upLeft, wall)
        result = result or self.playerLineIntersectsWall(currentBorder.upRight, nextBorder.upRight, wall)

        return result

    def playerCanStepOverWall(self, player, wall):
        return wall.height <= player.maxStepHeight

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
            return wall.startPoint.x <= x and x <= wall.endPoint.x
        elif wall.orientation == Orientation.vertical:
            return wall.startPoint.y <= y and y <= wall.endPoint.y
        elif wall.orientation == Orientation.diagonal:
            return Geometry.lineContainsPoint(wall.startPoint.x, wall.startPoint.y, wall.endPoint.x, wall.endPoint.y, x, y)
        else:
            raise Exception()


def makePlayerWallCollisionDetector(resolver):
    return PlayerWallCollisionDetector(resolver.resolve(GameData))
