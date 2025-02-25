from game.engine.GameData import GameData


class CameraUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        camera = self.gameData.camera
        camera.position = self.gameData.player.eyePosition
        camera.lookDirection = self.gameData.player.lookDirection
        camera.calculateViewMatrix()
        camera.setVerticalViewRadians(self.gameData.aimState.verticalViewRadians)
        camera.calculateProjectionMatrix()


def makeCameraUpdater(resolver):
    return CameraUpdater(resolver.resolve(GameData))
