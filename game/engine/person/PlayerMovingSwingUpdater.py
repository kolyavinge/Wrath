from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.person.PersonState import PersonState


class PlayerMovingSwingUpdater:

    def __init__(self, gameData):
        self.gameData = gameData
        self.movingParam = 0

    def update(self):
        self.commitCurrentSwingValue()
        self.calculateSwingValue()
        self.updateLookSwing()
        self.updateLandingSwing()

    def commitCurrentSwingValue(self):
        player = self.gameData.player
        player.prevPrevSwingValue = player.prevSwingValue
        player.prevSwingValue = player.currentSwingValue

    def calculateSwingValue(self):
        player = self.gameData.player
        if player.state != PersonState.standing:
            self.movingParam = 0
        elif player.velocityValue == 0:
            self.movingParam = 0
        else:
            self.movingParam += 0.1
        player.currentSwingValue = 0.2 * player.velocityValue * Math.sin(4.0 * self.movingParam)

    def updateLookSwing(self):
        player = self.gameData.player
        if player.currentSwingValue != 0:
            swingDirection = player.lookDirectionNormal.copy()
            swingDirection.mul(player.currentSwingValue)
            player.eyePosition.add(swingDirection)

    def updateLandingSwing(self):
        player = self.gameData.player
        if player.state == PersonState.landing:
            swingValue = 0.5 * player.landingTime * Math.sin(4.0 * player.landingTime)
            player.eyePosition.z += swingValue


def makePlayerMovingSwingUpdater(resolver):
    return PlayerMovingSwingUpdater(resolver.resolve(GameData))
