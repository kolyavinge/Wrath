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
        player = self.gameData.player
        if not player.hasMoved:
            return

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.walls:
                if wall.orientation == Orientation.horizontal or wall.orientation == Orientation.vertical:
                    self.processWall(wall)

        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.walls:
                if wall.orientation == Orientation.diagonal:
                    self.processWall(wall)

    def processWall(self, wall):
        currentBorder = self.gameData.player.currentBorder.bottom
        nextBorder = self.gameData.player.nextBorder.bottom
        self.processPlayerLine(currentBorder.downLeft, nextBorder.downLeft, wall)
        self.processPlayerLine(currentBorder.downRight, nextBorder.downRight, wall)
        self.processPlayerLine(currentBorder.upLeft, nextBorder.upLeft, wall)
        self.processPlayerLine(currentBorder.upRight, nextBorder.upRight, wall)

    def processPlayerLine(self, playerPointFrom, playerPointTo, wall):
        if self.isPlayerPointBehindWall(playerPointTo, wall):
            intersectPoint = self.getWallIntersectPointOrNone(playerPointFrom, playerPointTo, wall)
            if intersectPoint is not None:
                if self.playerLineContainsPoint(playerPointFrom, playerPointTo, intersectPoint) and self.wallContainsPoint(wall, intersectPoint):
                    player = self.gameData.player
                    x, y = self.getPointOnLimitLine(wall, player.nextCenterPoint)
                    player.moveNextPositionTo(Vector3(x, y, player.getZ()))
                    player.forwardMovingTime /= 2
                    player.backwardMovingTime /= 2
                    player.leftStepMovingTime /= 2
                    player.rightStepMovingTime /= 2
                    self.hasCollisions = True

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

    def getPointOnLimitLine(self, wall, playerNextCenterPoint):
        if wall.orientation == Orientation.horizontal:
            return (playerNextCenterPoint.x, wall.limitLine.startPoint.y)
        elif wall.orientation == Orientation.vertical:
            return (wall.limitLine.startPoint.x, playerNextCenterPoint.y)
        elif wall.orientation == Orientation.diagonal:
            playerDirection = wall.limitLine.startPoint.getDirectionTo(playerNextCenterPoint)
            projected = Geometry.getProjectedVector(playerDirection, wall.limitLineDirection)
            projected.add(wall.limitLine.startPoint)

            return (projected.x, projected.y)
        else:
            raise Exception()


def makePlayerWallCollisionProcessor(resolver):
    return PlayerWallCollisionProcessor(resolver.resolve(GameData))
