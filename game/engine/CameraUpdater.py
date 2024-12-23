from game.engine.GameData import GameData


class CameraUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        self.gameData.camera.position = self.gameData.player.eyePosition
        self.gameData.camera.lookDirection = self.gameData.player.lookDirection
        self.gameData.camera.calculateViewMatrix()

    # def updateIfPlayerMoved(self):
    #     if self.gameData.player.hasMoved or self.gameData.player.hasTurned:
    #         self.update()
    #         self.gameData.camera.calculateViewMatrix()


def makeCameraUpdater(resolver):
    return CameraUpdater(resolver.resolve(GameData))
