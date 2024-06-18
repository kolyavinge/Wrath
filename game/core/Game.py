from game.engine.GameData import GameData
from game.engine.LevelManager import LevelManager
from game.input.InputManager import InputManager
from game.render.debug.DebugRenderer import DebugRenderer
from game.ui.ScreenManager import ScreenManager


class Game:

    def __init__(self, levelManager, inputManager, screenManager, debugRenderer):
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.debugRenderer = debugRenderer
        self.levelManager.loadFirstLevel()  # TODO: временно

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput()
        self.screenManager.currentScreen.update()

    def renderCurrentScreen(self):
        self.debugRenderer.render()

    def voxCurrentScreen(self):
        pass


def makeGame(resolver):
    return Game(resolver.resolve(LevelManager), resolver.resolve(InputManager), resolver.resolve(ScreenManager), resolver.resolve(DebugRenderer))
