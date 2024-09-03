from game.anx.PlayerConstants import PlayerConstants
from game.engine.GameData import GameData


class CameraUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def updatePosition(self):
        self.gameData.camera.position = self.gameData.player.currentCenterPoint.copy()
        self.gameData.camera.position.z += PlayerConstants.eyeLength
        self.gameData.camera.lookDirection = self.gameData.player.lookDirection

    def updatePositionIfPlayerMoved(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned:
            self.updatePosition()

    def calculateViewMatrix(self):
        self.gameData.camera.calculateViewMatrix()

    def calculateViewMatrixIfPlayerMoved(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned:
            self.calculateViewMatrix()


def makeCameraUpdater(resolver):
    return CameraUpdater(resolver.resolve(GameData))
