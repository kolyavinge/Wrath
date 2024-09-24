from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.Orientation import Orientation


class CollisionResult:

    def __init__(self, wall, distance):
        self.wall = wall
        self.distance = distance


class PlayerWallCollisionDetector2:

    def __init__(self, gameData):
        self.gameData = gameData

    def detectCollisions(self):
        self.gameData.playerCollidedWalls = []

        player = self.gameData.player
        if not player.hasMoved:
            return

        collidedWalls = []
        for levelSegment in player.collisionLevelSegments:
            for wall in levelSegment.walls:
                distance = self.getCollisionDistance(player, wall)
                if distance < CommonConstants.maxLevelSize:
                    collidedWalls.append(CollisionResult(wall, distance))

        if len(collidedWalls) > 0:
            collidedWalls.sort(key=lambda x: x.distance)
            self.gameData.playerCollidedWalls = list(map(lambda x: x.wall, collidedWalls))

    def getCollisionDistance(self, player, wall):
        currentBorder = player.currentBorder.bottom
        nextBorder = player.nextBorder.bottom

        distance1 = self.getIntersectDistance(currentBorder.downLeft, nextBorder.downLeft, wall)
        distance2 = self.getIntersectDistance(currentBorder.downRight, nextBorder.downRight, wall)
        distance3 = self.getIntersectDistance(currentBorder.upLeft, nextBorder.upLeft, wall)
        distance4 = self.getIntersectDistance(currentBorder.upRight, nextBorder.upRight, wall)

        result = self.getMinDistance(distance1, distance2, distance3, distance4)

        return result

    def hasCollision(self, player, wall):
        return self.getCollisionDistance(player, wall) < CommonConstants.maxLevelSize

    def getIntersectDistance(self, playerPointFrom, playerPointTo, wall):
        if self.isPlayerPointBehindWall(playerPointTo, wall):
            intersectPoint = self.getWallIntersectPointOrNone(playerPointFrom, playerPointTo, wall)
            if intersectPoint is not None:
                if self.playerLineContainsPoint(playerPointFrom, playerPointTo, intersectPoint) and self.wallContainsPoint(wall, intersectPoint):
                    intersectPointX, intersectPointY = intersectPoint
                    intersectDirection = Vector3(intersectPointX, intersectPointY, 0)
                    intersectDirection.sub(playerPointFrom)
                    intersectDirection.z = 0
                    return intersectDirection.getLength()

        return CommonConstants.maxLevelSize

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

    def getMinDistance(self, distance1, distance2, distance3, distance4):
        return Math.min(Math.min(distance1, distance2), Math.min(distance3, distance4))


def makePlayerWallCollisionDetector2(resolver):
    return PlayerWallCollisionDetector2(resolver.resolve(GameData))
