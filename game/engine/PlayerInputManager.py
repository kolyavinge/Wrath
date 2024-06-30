from game.engine.PlayerMoveLogic import PlayerMoveLogic
from game.engine.PlayerTurnLogic import PlayerTurnLogic
from game.input.InputManager import InputManager
from game.input.Keys import Keys
from game.lib.Math import Math


class PlayerInputManager:

    def __init__(self, playerMoveLogic, playerTurnLogic, inputManager):
        self.playerMoveLogic = playerMoveLogic
        self.playerTurnLogic = playerTurnLogic
        self.inputManager = inputManager

    def processInput(self):
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        keyboard = self.inputManager.keyboard

        if keyboard.isPressedOrHeld(Keys.w):
            self.playerMoveLogic.goForward()
        elif keyboard.isPressedOrHeld(Keys.s):
            self.playerMoveLogic.goBackward()

        if keyboard.isPressedOrHeld(Keys.a):
            self.playerMoveLogic.stepLeft()
        elif keyboard.isPressedOrHeld(Keys.d):
            self.playerMoveLogic.stepRight()

    def processMouse(self):
        mouse = self.inputManager.mouse

        if mouse.dx < 0:
            self.playerTurnLogic.turnLeft(0.005 * Math.abs(mouse.dx))
        elif mouse.dx > 0:
            self.playerTurnLogic.turnRight(0.005 * Math.abs(mouse.dx))

        if mouse.dy < 0:
            self.playerTurnLogic.lookUp(0.005 * Math.abs(mouse.dy))
        elif mouse.dy > 0:
            self.playerTurnLogic.lookDown(0.005 * Math.abs(mouse.dy))


def makePlayerInputManager(resolver):
    return PlayerInputManager(resolver.resolve(PlayerMoveLogic), resolver.resolve(PlayerTurnLogic), resolver.resolve(InputManager))
