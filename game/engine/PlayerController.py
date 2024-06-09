from game.lib.Math import Math
from game.calc.Geometry import Geometry
from game.anx.Constants import Constants
from game.engine.GameData import GameData


class PlayerController:

    def __init__(self, gameData):
        self.gameData = gameData

    def goForward(self):
        player = self.gameData.player
        player.hasMoved = True
        velocityDirection = player.frontNormal.getCopy()
        velocityDirection.setLength(player.getVelocity())
        player.centerPoint.add(velocityDirection)
        player.movingTime += player.movingTimeDelta

    def goBackward(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.frontNormal.getCopy()
        delta.setLength(0.1)
        player.centerPoint.sub(delta)

    def stepLeft(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.rightNormal.getCopy()
        delta.setLength(0.1)
        player.centerPoint.sub(delta)

    def stepRight(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.rightNormal.getCopy()
        delta.setLength(0.1)
        player.centerPoint.add(delta)

    def turnLeft(self, radians):
        player = self.gameData.player
        player.hasMoved = True
        player.lookDirection = Geometry.rotatePoint(player.lookDirection, Constants.zAxis, Constants.axisOrigin, radians)
        player.lookDirection.normalized()
        player.frontNormal = Geometry.rotatePoint(player.frontNormal, Constants.zAxis, Constants.axisOrigin, radians)
        player.frontNormal.normalized()
        player.rightNormal = player.frontNormal.getCopy()
        player.rightNormal.vectorProduct(Constants.zAxis)

    def turnRight(self, radians):
        player = self.gameData.player
        player.hasMoved = True
        player.lookDirection = Geometry.rotatePoint(player.lookDirection, Constants.zAxis, Constants.axisOrigin, -radians)
        player.lookDirection.normalized()
        player.frontNormal = Geometry.rotatePoint(player.frontNormal, Constants.zAxis, Constants.axisOrigin, -radians)
        player.frontNormal.normalized()
        player.rightNormal = player.frontNormal.getCopy()
        player.rightNormal.vectorProduct(Constants.zAxis)

    def lookUp(self, radians):
        player = self.gameData.player
        player.hasMoved = True
        player.lookDirection = Geometry.rotatePoint(player.lookDirection, Constants.xAxis, Constants.axisOrigin, radians)
        player.lookDirection.normalized()
        dotProduct = player.lookDirection.dotProduct(player.frontNormal)
        if dotProduct <= 0:
            player.lookDirection = Geometry.rotatePoint(player.frontNormal, Constants.xAxis, Constants.axisOrigin, Math.piHalf - 0.1)
            player.lookDirection.normalized()

    def lookDown(self, radians):
        player = self.gameData.player
        player.hasMoved = True
        player.lookDirection = Geometry.rotatePoint(player.lookDirection, Constants.xAxis, Constants.axisOrigin, -radians)
        player.lookDirection.normalized()
        dotProduct = player.lookDirection.dotProduct(player.frontNormal)
        if dotProduct <= 0:
            player.lookDirection = Geometry.rotatePoint(player.frontNormal, Constants.xAxis, Constants.axisOrigin, -(Math.piHalf - 0.1))
            player.lookDirection.normalized()


def makePlayerController(resolver):
    return PlayerController(resolver.resolve(GameData))
