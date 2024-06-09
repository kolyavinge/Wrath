from game.engine.GameUpdater import GameUpdater
from game.engine.PlayerInputManager import PlayerInputManager


class GameScreen:

    def __init__(self, gameUpdater, playerInputManager):
        self.gameUpdater = gameUpdater
        self.playerInputManager = playerInputManager

    def update(self):
        self.gameUpdater.update()

    def processInput(self):
        self.playerInputManager.processInput()


def makeGameScreen(resolver):
    return GameScreen(resolver.resolve(GameUpdater), resolver.resolve(PlayerInputManager))
