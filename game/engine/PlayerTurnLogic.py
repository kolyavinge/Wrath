from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math


class PlayerTurnLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        inputData = self.gameData.playerInputData

        if inputData.turnLeftRadians > 0:
            self.turnLeft(inputData.turnLeftRadians)
        elif inputData.turnRightRadians > 0:
            self.turnRight(inputData.turnRightRadians)

        if inputData.lookUpRadians > 0:
            self.lookUp(inputData.lookUpRadians)
        elif inputData.lookDownRadians > 0:
            self.lookDown(inputData.lookDownRadians)

    def turnLeft(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasTurned = True
        player.yawRadians = Geometry.normalizeRadians(player.yawRadians + radians)
        self.calculateDirectionVectors()

    def turnRight(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasTurned = True
        player.yawRadians = Geometry.normalizeRadians(player.yawRadians - radians)
        self.calculateDirectionVectors()

    def lookUp(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasTurned = True
        player.pitchRadians = Geometry.normalizeRadians(player.pitchRadians + radians)
        if player.pitchRadians >= player.maxPitchRadians:
            player.pitchRadians = player.maxPitchRadians
        self.calculateDirectionVectors()

    def lookDown(self, radians):
        assert radians > 0
        player = self.gameData.player
        player.hasTurned = True
        player.pitchRadians = Geometry.normalizeRadians(player.pitchRadians - radians)
        if player.pitchRadians <= -player.maxPitchRadians:
            player.pitchRadians = -player.maxPitchRadians
        self.calculateDirectionVectors()

    def orientByFrontNormal(self, frontNormal):
        player = self.gameData.player
        radians = Math.arccos(player.frontNormal.dotProduct(frontNormal))
        vectorProduct = player.frontNormal.copy()
        vectorProduct.vectorProduct(frontNormal)
        if vectorProduct.z < 0:
            radians *= -1
        player.yawRadians = radians
        self.calculateDirectionVectors()

    def calculateDirectionVectors(self):
        player = self.gameData.player
        player.frontNormal = Geometry.rotatePoint(CommonConstants.yAxis, CommonConstants.zAxis, CommonConstants.axisOrigin, player.yawRadians)
        player.rightNormal = Geometry.rotatePoint(player.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        player.lookDirection = Geometry.rotatePoint(player.frontNormal, player.rightNormal, CommonConstants.axisOrigin, player.pitchRadians)


def makePlayerTurnLogic(resolver):
    return PlayerTurnLogic(resolver.resolve(GameData))
