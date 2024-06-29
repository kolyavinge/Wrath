from game.engine.GameData import GameData
from game.model.PlayerMeasures import PlayerMeasures


class CameraUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        self.gameData.camera.position = self.gameData.player.currentCenterPoint.getCopy()
        self.gameData.camera.position.z += PlayerMeasures.eyeLength
        self.gameData.camera.lookDirection = self.gameData.player.lookDirection
        self.gameData.camera.calculateViewMatrix()


def makeCameraUpdater(resolver):
    return CameraUpdater(resolver.resolve(GameData))
