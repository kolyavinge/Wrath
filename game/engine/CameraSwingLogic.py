from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.PlayerState import PlayerState


class CameraSwingLogic:

    def __init__(self, gameData):
        self.gameData = gameData
        self.movingParam = 0

    def updateSwing(self):
        self.movingSwing()
        self.landingSwing()

    def movingSwing(self):
        player = self.gameData.player
        if player.state != PlayerState.standing:
            self.movingParam = 0
            return
        if player.velocityValue == 0:
            self.movingParam = 0
            return

        self.movingParam += 0.1
        swingValue = 0.2 * player.velocityValue * Math.sin(4.0 * self.movingParam)
        swingDirection = player.lookDirectionNormal.copy()
        swingDirection.mul(swingValue)
        self.gameData.camera.position.add(swingDirection)

    def landingSwing(self):
        player = self.gameData.player
        if player.state != PlayerState.landing:
            return

        swingValue = 0.5 * player.landingTime * Math.sin(4.0 * player.landingTime)
        self.gameData.camera.position.z += swingValue


def makeCameraSwingLogic(resolver):
    return CameraSwingLogic(resolver.resolve(GameData))
