from game.engine.level.LevelUpdater import LevelUpdater
from game.input.InputManager import InputManager


class GameScreen:

    def __init__(self, levelUpdater, inputManager):
        self.levelUpdater = levelUpdater
        self.inputManager = inputManager

    def update(self):
        self.levelUpdater.update()

    def processInput(self):
        pass


def makeGameScreen(resolver):
    return GameScreen(resolver.resolve(LevelUpdater), resolver.resolve(InputManager))
