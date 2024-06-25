from game.engine.GameData import GameData


class PlayerPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        if player.hasMoved:
            player.hasMoved = False
            player.commitNextPosition()


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData))
