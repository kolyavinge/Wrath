from game.lib.Math import Math
from game.engine.PlayerController import PlayerController
from game.input.Keys import Keys
from game.input.InputManager import InputManager


class PlayerInputManager:

    def __init__(self, playerController, inputManager):
        self.playerController = playerController
        self.inputManager = inputManager

    def processInput(self):
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        keyboard = self.inputManager.keyboard

        if keyboard.isPressedOrHeld(Keys.w):
            self.playerController.goForward()
        elif keyboard.isPressedOrHeld(Keys.s):
            self.playerController.goBackward()

        if keyboard.isPressedOrHeld(Keys.a):
            self.playerController.stepLeft()
        elif keyboard.isPressedOrHeld(Keys.d):
            self.playerController.stepRight()

    def processMouse(self):
        mouse = self.inputManager.mouse

        if mouse.dx < 0:
            self.playerController.turnLeft(0.005 * Math.abs(mouse.dx))
        elif mouse.dx > 0:
            self.playerController.turnRight(0.005 * Math.abs(mouse.dx))

        if mouse.dy < 0:
            self.playerController.lookUp(0.005 * Math.abs(mouse.dy))
        elif mouse.dy > 0:
            self.playerController.lookDown(0.005 * Math.abs(mouse.dy))


def makePlayerInputManager(resolver):
    return PlayerInputManager(resolver.resolve(PlayerController), resolver.resolve(InputManager))
