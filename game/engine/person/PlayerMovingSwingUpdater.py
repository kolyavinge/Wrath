from game.lib.Math import Math
from game.model.person.PersonStates import PersonZState


class PlayerMovingSwingUpdater:

    def __init__(self):
        self.movingParam = 0

    def update(self, gameState):
        self.calculateSwingValue(gameState.player)
        self.updateLookSwing(gameState.player)
        self.updateLandingSwing(gameState.player)

    def calculateSwingValue(self, player):
        if player.zState != PersonZState.onFloor:
            self.movingParam = 0
        elif player.velocityValue == 0:
            self.movingParam = 0
        else:
            self.movingParam += 0.1
        player.swingValue = 0.2 * player.velocityValue * Math.sin(4.0 * self.movingParam)

    def updateLookSwing(self, player):
        if player.swingValue != 0:
            swingDirection = player.lookDirectionNormal.copy()
            swingDirection.mul(player.swingValue)
            player.eyePosition.add(swingDirection)

    def updateLandingSwing(self, player):
        if player.zState == PersonZState.landing:
            swingValue = 0.5 * player.landingTime * Math.sin(4.0 * player.landingTime)
            player.eyePosition.z += swingValue  # TODO не работает
