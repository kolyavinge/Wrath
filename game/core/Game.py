from game.engine.level.LevelManager import LevelManager
from game.input.InputManager import InputManager
from game.ui.ScreenManager import ScreenManager


class Game:

    def __init__(self, levelManager, inputManager, screenManager):
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager

    def startLevel(self):
        self.levelManager.loadLevel()
        self.currentLevel = self.levelManager.currentLevel

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.update()
        self.screenManager.currentScreen.processInput()


def makeGame(resolver):
    return Game(resolver.resolve(LevelManager), resolver.resolve(InputManager), resolver.resolve(ScreenManager))
