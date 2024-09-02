from game.core.GameInitializer import GameInitializer
from game.core.ScreenManager import ScreenManager
from game.engine.LevelManager import LevelManager
from game.input.InputManager import InputManager
from game.render.debug.DebugRenderer import DebugRenderer


class Game:

    def __init__(self, gameInitializer, levelManager, inputManager, screenManager, debugRenderer):
        gameInitializer.init()
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.debugRenderer = debugRenderer
        self.levelManager.loadFirstLevel()  # TODO: временно
        self.screenManager.currentScreenRenderer.init()

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput()
        self.screenManager.currentScreen.update()

    def renderCurrentScreen(self):
        self.debugRenderer.render()
        self.screenManager.currentScreenRenderer.render()

    def voxCurrentScreen(self):
        pass


def makeGame(resolver):
    return Game(
        resolver.resolve(GameInitializer),
        resolver.resolve(LevelManager),
        resolver.resolve(InputManager),
        resolver.resolve(ScreenManager),
        resolver.resolve(DebugRenderer),
    )
