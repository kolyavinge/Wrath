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
        assert radians > 0
        player = self.gameData.player
        player.hasMoved = True
        player.yawRadians = Geometry.normalizeRadians(player.yawRadians + radians)
        self.calculateDirectionVectors()

    def turnRight(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasMoved = True
        player.yawRadians = Geometry.normalizeRadians(player.yawRadians - radians)
        self.calculateDirectionVectors()

    def lookUp(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasMoved = True
        player.pitchRadians = Geometry.normalizeRadians(player.pitchRadians + radians)
        if player.pitchRadians >= player.maxPitchRadians:
            player.pitchRadians = player.maxPitchRadians
        self.calculateDirectionVectors()

    def lookDown(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasMoved = True
        player.pitchRadians = Geometry.normalizeRadians(player.pitchRadians - radians)
        if player.pitchRadians <= -player.maxPitchRadians:
            player.pitchRadians = -player.maxPitchRadians
        self.calculateDirectionVectors()

    def calculateDirectionVectors(self):
        player = self.gameData.player
        player.frontNormal = Geometry.rotatePoint(Constants.yAxis, Constants.zAxis, Constants.axisOrigin, player.yawRadians)
        player.rightNormal = Geometry.rotatePoint(player.frontNormal, Constants.zAxis, Constants.axisOrigin, -Math.piHalf)
        player.lookDirection = Geometry.rotatePoint(player.frontNormal, player.rightNormal, Constants.axisOrigin, player.pitchRadians)


def makePlayerController(resolver):
    return PlayerController(resolver.resolve(GameData))
