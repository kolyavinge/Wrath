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
        if len(self.gameData.playerCollidedWalls) == 0:
            return

        self.processWall(self.gameData.playerCollidedWalls[0])

        player = self.gameData.player
        for i in range(1, len(self.gameData.playerCollidedWalls)):
            wall = self.gameData.playerCollidedWalls[i]
            if self.playerWallCollisionDetector.hasCollision(player, wall):
                self.processWall(wall)

    def processWall(self, wall):
        player = self.gameData.player
        x, y = self.getPointOnLimitLine(wall, player.nextCenterPoint)
        newNextPosition = Vector3(Math.round(x, 2), Math.round(y, 2), player.getZ())
        player.moveNextPositionTo(newNextPosition)
        player.forwardMovingTime /= 2
        player.backwardMovingTime /= 2
        player.leftStepMovingTime /= 2
        player.rightStepMovingTime /= 2

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
