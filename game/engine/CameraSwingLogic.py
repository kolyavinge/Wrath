from game.engine.GameData import GameData
from game.lib.Math import Math


class CameraSwingLogic:

    def __init__(self, gameData):
        self.gameData = gameData
        self.sinParam = 0

    def updateSwing(self):
        player = self.gameData.player
        if player.velocityValue == 0:
            self.sinParam = 0
            return

        self.sinParam += 0.1
        swingValue = 0.2 * player.velocityValue * Math.sin(4.0 * self.sinParam)
        swingDirection = player.lookDirectionNormal.copy()
        swingDirection.mul(swingValue)
        self.gameData.camera.position.add(swingDirection)


def makeCameraSwingLogic(resolver):
    return CameraSwingLogic(resolver.resolve(GameData))
