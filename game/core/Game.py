from game.core.Client import Client
from game.core.GameInitializer import GameInitializer
from game.core.GameStartMode import GameStartMode
from game.core.ScreenManager import ScreenManager
from game.core.Server import Server
from game.input.InputManager import InputManager
from game.lib.EventManager import EventManager


class Game:

    def __init__(
        self,
        gameInitializer: GameInitializer,
        inputManager: InputManager,
        screenManager: ScreenManager,
        eventManager: EventManager,  # for App
    ):
        self.gameInitializer = gameInitializer
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.eventManager = eventManager
        self.client = None
        self.server = None

    def init(self, gameStartMode):
        print("GameStartMode", gameStartMode)
        self.client = Client()
        if gameStartMode == GameStartMode.clientServerMode:
            self.server = Server()
        self.gameInitializer.init(gameStartMode, self.client, self.server)
        self.screenManager.currentScreenRenderer.init(self.client.gameState)
        self.screenManager.currentScreenVox.init(self.client.gameState)

    def updateCurrentScreen(self):
        self.inputManager.update()
        self.screenManager.currentScreen.processInput(self.client.gameState)
        self.screenManager.currentScreen.update()

    def renderCurrentScreen(self):
        self.screenManager.currentScreenRenderer.render(self.client.gameState)

    def voxCurrentScreen(self):
        self.screenManager.currentScreenVox.update(self.client.gameState)
