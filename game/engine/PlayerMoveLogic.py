from game.engine.GameData import GameData


class PlayerMoveLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        player = self.gameData.player
        if player.velocityValue > 0:
            player.hasMoved = True
            self.updateDoStep()
            player.moveNextPositionBy(player.velocityVector)

    def updateDoStep(self):
        player = self.gameData.player
        player.doStep = (
            player.prevPrevSwingValue < 0
            and player.prevSwingValue < 0
            and player.currentSwingValue < 0
            and player.prevPrevSwingValue > player.prevSwingValue
            and player.currentSwingValue > player.prevSwingValue
        )


def makePlayerMoveLogic(resolver):
    return PlayerMoveLogic(resolver.resolve(GameData))
