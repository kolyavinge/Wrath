from game.engine.level.LevelManager import LevelManager
from game.ui.ScreenManager import ScreenManager


class Game:

    def __init__(self, levelManager, screenManager):
        self.levelManager = levelManager
        self.screenManager = screenManager

    def startLevel(self):
        self.levelManager.loadLevel()
        self.currentLevel = self.levelManager.getCurrentLevel()

    def updateCurrentScreen(self):
        self.screenManager.currentScreen.update()
        self.screenManager.currentScreen.processInput()


def makeGame(resolver):
    return Game(resolver.resolve(LevelManager), resolver.resolve(ScreenManager))
