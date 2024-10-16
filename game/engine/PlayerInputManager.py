from game.engine.GameData import GameData
from game.input.InputManager import InputManager
from game.input.Keys import Keys
from game.lib.Math import Math


class PlayerInputManager:

    def __init__(self, gameData, inputManager):
        self.gameData = gameData
        self.inputManager = inputManager

    def processInput(self):
        self.gameData.playerInputData.clear()
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        inputData = self.gameData.playerInputData
        keyboard = self.inputManager.keyboard

        if keyboard.isPressedOrHeld(Keys.w):
            inputData.goForward = True
        elif keyboard.isPressedOrHeld(Keys.s):
            inputData.goBackward = True

        if keyboard.isPressedOrHeld(Keys.a):
            inputData.stepLeft = True
        elif keyboard.isPressedOrHeld(Keys.d):
            inputData.stepRight = True

        if keyboard.isPressed(Keys.f):
            inputData.torchSwitch = True

    def processMouse(self):
        inputData = self.gameData.playerInputData
        mouse = self.inputManager.mouse

        if mouse.dx < 0:
            inputData.turnLeftRadians = 0.005 * Math.abs(mouse.dx)
        elif mouse.dx > 0:
            inputData.turnRightRadians = 0.005 * Math.abs(mouse.dx)

        if mouse.dy < 0:
            inputData.lookUpRadians = 0.005 * Math.abs(mouse.dy)
        elif mouse.dy > 0:
            inputData.lookDownRadians = 0.005 * Math.abs(mouse.dy)

        if mouse.isLeftButtonPressed():
            inputData.fire = True


def makePlayerInputManager(resolver):
    return PlayerInputManager(resolver.resolve(GameData), resolver.resolve(InputManager))
