from game.engine.GameData import GameData


class CameraUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        self.gameData.camera.position = self.gameData.player.centerPoint.getCopy()
        self.gameData.camera.position.z += 0.5
        self.gameData.camera.lookDirection = self.gameData.player.lookDirection
        self.gameData.camera.calculateViewMatrix()


def makeCameraUpdater(resolver):
    return CameraUpdater(resolver.resolve(GameData))
