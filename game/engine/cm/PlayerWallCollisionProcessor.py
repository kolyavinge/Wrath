from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.cm.PlayerWallCollisionDetector import PlayerWallCollisionDetector
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.Orientation import Orientation


class PlayerWallCollisionProcessor:

    def __init__(self, gameData, playerWallCollisionDetector):
        self.gameData = gameData
        self.playerWallCollisionDetector = playerWallCollisionDetector

    def processCollisions(self):
        collidedWalls = self.playerWallCollisionDetector.getCollidedWalls()
        if len(collidedWalls) == 0:
            return

        self.processWall(collidedWalls[0])

        player = self.gameData.player
        for i in range(1, len(collidedWalls)):
            wall = collidedWalls[i]
            if self.playerWallCollisionDetector.hasCollision(player, wall):
                self.processWall(wall)

    def processWall(self, wall):
        player = self.gameData.player
        x, y = self.getPointOnLimitLine(wall, player.nextCenterPoint)
        newNextPosition = Vector3(Math.round(x, 2), Math.round(y, 2), player.getZ())
        player.moveNextPositionTo(newNextPosition)

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
            raise Exception("Wrong wall orientation.")


def makePlayerWallCollisionProcessor(resolver):
    return PlayerWallCollisionProcessor(resolver.resolve(GameData), resolver.resolve(PlayerWallCollisionDetector))
