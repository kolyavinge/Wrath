from game.engine.GameUpdater import GameUpdater
from game.input.InputManager import InputManager


class GameScreen:

    def __init__(self, gameUpdater, inputManager):
        self.gameUpdater = gameUpdater
        self.inputManager = inputManager

    def update(self):
        self.gameUpdater.update()

    def processInput(self):
        pass


def makeGameScreen(resolver):
    return GameScreen(resolver.resolve(GameUpdater), resolver.resolve(InputManager))
