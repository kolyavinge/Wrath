from game.core.GameInitializer import GameInitializer
from game.core.ScreenManager import ScreenManager
from game.input.InputManager import InputManager
from game.lib.EventManager import EventManager
from game.network.Client import Client
from game.network.Server import Server


class Game:

    def __init__(
        self,
        gameInitializer: GameInitializer,
        inputManager: InputManager,
        screenManager: ScreenManager,
        eventManager: EventManager,  # for App
    ):
        self.inputManager = inputManager
        self.screenManager = screenManager
        self.eventManager = eventManager
        self.client = Client()
        self.server = Server()
        gameInitializer.init(self.client, self.server)
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
