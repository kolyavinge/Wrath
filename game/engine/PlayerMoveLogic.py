from game.engine.GameData import GameData


class PlayerMoveLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        player = self.gameData.player
        if player.velocityValue > 0:
            player.hasMoved = True
            player.moveNextPositionBy(player.velocityVector)


def makePlayerMoveLogic(resolver):
    return PlayerMoveLogic(resolver.resolve(GameData))
