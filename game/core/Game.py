from game.core.GameInitializer import GameInitializer
from game.core.ScreenManager import ScreenManager
from game.engine.level.LevelManager import LevelManager
from game.input.InputManager import InputManager
from game.lib.EventManager import EventManager


class Game:

    def __init__(
        self,
        gameInitializer: GameInitializer,
        levelManager: LevelManager,
        inputManager: InputManager,
        screenManager: ScreenManager,
        eventManager: EventManager,
    ):
        gameInitializer.init()
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.levelManager.loadFirstLevel()  # TODO: временно
        self.screenManager.currentScreenRenderer.init()
        self.screenManager.currentScreenVox.init()
        self.eventManager = eventManager

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput()
        self.screenManager.currentScreen.update()

    def updateEnemyAI(self):
        self.screenManager.currentScreen.updateEnemyAI()

    def renderCurrentScreen(self):
        self.screenManager.currentScreenRenderer.render()

    def voxCurrentScreen(self):
        self.screenManager.currentScreenVox.update()
