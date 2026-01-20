from game.core.GameInitializer import GameInitializer
from game.core.ScreenManager import ScreenManager
from game.engine.GameState import GameState
from game.engine.level.LevelManager import LevelManager
from game.input.InputManager import InputManager
from game.lib.EventManager import EventManager
from game.network.Client import Client
from game.network.Server import Server


class Game:

    def __init__(
        self,
        gameState: GameState,
        gameInitializer: GameInitializer,
        levelManager: LevelManager,
        inputManager: InputManager,
        screenManager: ScreenManager,
        eventManager: EventManager,  # for App
    ):
        self.client = Client()
        self.client.gameState = gameState  # TODO delete
        self.server = Server()
        gameInitializer.init(self.client, self.server)
        self.levelManager = levelManager
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.levelManager.loadFirstLevel(gameState)  # TODO: временно
        self.screenManager.currentScreenRenderer.init(gameState)
        self.screenManager.currentScreenVox.init(gameState)
        self.eventManager = eventManager

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput(self.client.gameState)
        self.screenManager.currentScreen.update()

    def renderCurrentScreen(self):
        self.screenManager.currentScreenRenderer.render()

    def voxCurrentScreen(self):
        self.screenManager.currentScreenVox.update(self.client.gameState)
