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

        if keyboard.isPressed(Keys.w):
            self.playerController.goForward()
        elif keyboard.isPressed(Keys.s):
            self.playerController.goBackward()

        if keyboard.isPressed(Keys.a):
            self.playerController.stepLeft()
        elif keyboard.isPressed(Keys.d):
            self.playerController.stepRight()

    def processMouse(self):
        mouse = self.inputManager.mouse

        if mouse.dx < 0:
            self.playerController.turnLeft(Math.abs(mouse.dx))
        elif mouse.dx > 0:
            self.playerController.turnRight(Math.abs(mouse.dx))

        if mouse.dy > 0:
            self.playerController.lookUp(Math.abs(mouse.dy))
        elif mouse.dy < 0:
            self.playerController.lookDown(Math.abs(mouse.dy))


def makePlayerInputManager(resolver):
    return PlayerInputManager(resolver.resolve(PlayerController), resolver.resolve(InputManager))
