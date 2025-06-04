from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.person.PersonZState import PersonZState


class PlayerMovingSwingUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData
        self.movingParam = 0

    def update(self):
        self.calculateSwingValue()
        self.updateLookSwing()
        self.updateLandingSwing()

    def calculateSwingValue(self):
        player = self.gameData.player
        if player.zState != PersonZState.onFloor:
            self.movingParam = 0
        elif player.velocityValue == 0:
            self.movingParam = 0
        else:
            self.movingParam += 0.1
        player.swingValue = 0.2 * player.velocityValue * Math.sin(4.0 * self.movingParam)

    def updateLookSwing(self):
        player = self.gameData.player
        if player.swingValue != 0:
            swingDirection = player.lookDirectionNormal.copy()
            swingDirection.mul(player.swingValue)
            player.eyePosition.add(swingDirection)

    def updateLandingSwing(self):
        player = self.gameData.player
        if player.zState == PersonZState.landing:
            swingValue = 0.5 * player.landingTime * Math.sin(4.0 * player.landingTime)
            player.eyePosition.z += swingValue
