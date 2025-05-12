from game.engine.GameUpdater import GameUpdater
from game.input.InputManager import InputManager
from game.input.PlayerInputManager import PlayerInputManager


class GameScreen:

    def __init__(self, gameUpdater, playerInputManager, inputManager):
        self.gameUpdater = gameUpdater
        self.playerInputManager = playerInputManager
        self.inputManager = inputManager

    def activate(self):
        self.inputManager.mouse.resetCursorPosition()

    def update(self):
        self.gameUpdater.update()

    def processInput(self):
        self.playerInputManager.processInput()


def makeGameScreen(resolver):
    return GameScreen(resolver.resolve(GameUpdater), resolver.resolve(PlayerInputManager), resolver.resolve(InputManager))
