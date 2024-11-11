from game.engine.GameData import GameData
from game.model.person.PlayerState import PlayerState


class PlayerPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        player.hasTurned = False
        if player.hasMoved:
            player.commitNextPosition()
            if player.state == PlayerState.standing:
                player.hasMoved = False


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData))
