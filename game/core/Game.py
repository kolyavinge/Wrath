from game.engine.LevelManager import LevelManager
from game.engine.GameData import GameData
from game.input.InputManager import InputManager
from game.ui.ScreenManager import ScreenManager


class Game:

    def __init__(self, levelManager, inputManager, screenManager):
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.levelManager.loadFirstLevel()  # TODO: временно

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput()
        self.screenManager.currentScreen.update()

    def renderCurrentScreen(self):
        pass

    def voxCurrentScreen(self):
        pass


def makeGame(resolver):
    return Game(resolver.resolve(LevelManager), resolver.resolve(InputManager), resolver.resolve(ScreenManager))
