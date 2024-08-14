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
            for levelSegment in self.gameData.player.collisionLevelSegments:
                for wall in levelSegment.walls:
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
                    x, y = self.getPointOnCrossLine(wall, player.nextCenterPoint)
                    player.moveNextPositionTo(Vector3(x, y, player.getZ()))
                    self.hasCollisions = True

    def isPlayerPointBehindWall(self, playerPoint, wall):
        behindDirection = wall.collisionLine.startPoint.getDirectionTo(playerPoint)
        dotProduct = behindDirection.dotProduct(wall.frontNormal)

        return dotProduct < 0

    def getWallIntersectPointOrNone(self, playerPointFrom, playerPointTo, wall):
        return Geometry.getLinesIntersectPointOrNone(
            wall.collisionLine.startPoint.x,
            wall.collisionLine.startPoint.y,
            wall.collisionLine.endPoint.x,
            wall.collisionLine.endPoint.y,
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
        collisionLine = wall.collisionLine
        if wall.orientation == Orientation.horizontal:
            return collisionLine.startPoint.x <= x and x <= collisionLine.endPoint.x
        elif wall.orientation == Orientation.vertical:
            return collisionLine.startPoint.y <= y and y <= collisionLine.endPoint.y
        elif wall.orientation == Orientation.diagonal:
            return Geometry.lineContainsPoint(
                collisionLine.startPoint.x, collisionLine.startPoint.y, collisionLine.endPoint.x, collisionLine.endPoint.y, x, y
            )
        else:
            raise Exception()

    def getPointOnCrossLine(self, wall, playerNextCenterPoint):
        if wall.orientation == Orientation.horizontal:
            return (playerNextCenterPoint.x, wall.crossLine.startPoint.y)
        elif wall.orientation == Orientation.vertical:
            return (wall.crossLine.startPoint.x, playerNextCenterPoint.y)
        elif wall.orientation == Orientation.diagonal:
            playerDirection = wall.crossLine.startPoint.getDirectionTo(playerNextCenterPoint)
            projected = Geometry.getProjectedVector(playerDirection, wall.crossLineDirection)
            projected.add(wall.crossLine.startPoint)

            return (projected.x, projected.y)
        else:
            raise Exception()


def makePlayerWallCollisionProcessor(resolver):
    return PlayerWallCollisionProcessor(resolver.resolve(GameData))
