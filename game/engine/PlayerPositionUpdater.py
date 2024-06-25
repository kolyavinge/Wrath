from game.engine.GameData import GameData


class PlayerPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        if self.gameData.player.hasMoved:
            self.gameData.player.hasMoved = False
            self.gameData.player.commitNextPosition()


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData))
