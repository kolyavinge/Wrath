from game.anx.Events import Events
from game.engine.GameData import GameData
from game.engine.logic.AimStateSwitcher import AimStateSwitcher
from game.input.InputManager import InputManager
from game.input.Keys import Keys
from game.lib.EventManager import EventManager
from game.lib.Math import Math
from game.model.AimState import SniperAimState
from game.model.weapon.Sniper import Sniper


class PlayerInputManager:

    def __init__(self, gameData, inputManager, aimStateSwitcher, eventManager):
        self.gameData = gameData
        self.inputManager = inputManager
        self.aimStateSwitcher = aimStateSwitcher
        self.eventManager = eventManager

    def processInput(self):
        self.gameData.playerInputData.clear()
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        inputData = self.gameData.playerInputData
        keyboard = self.inputManager.keyboard

        if keyboard.isPressed(Keys.d1):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 1)
        elif keyboard.isPressed(Keys.d2):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 2)
        elif keyboard.isPressed(Keys.d3):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 3)
        elif keyboard.isPressed(Keys.d4):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 4)
        elif keyboard.isPressed(Keys.d5):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 5)
        elif keyboard.isPressed(Keys.d6):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, 6)

        if keyboard.isPressedOrHeld(Keys.w):
            inputData.goForward = True
        elif keyboard.isPressedOrHeld(Keys.s):
            inputData.goBackward = True

        if keyboard.isPressedOrHeld(Keys.a):
            inputData.stepLeft = True
        elif keyboard.isPressedOrHeld(Keys.d):
            inputData.stepRight = True

        if keyboard.isPressed(Keys.f):
            self.eventManager.raiseEvent(Events.torchSwitchRequested)

    def processMouse(self):
        inputData = self.gameData.playerInputData
        mouse = self.inputManager.mouse
        aimState = self.gameData.aimState

        if mouse.dx < 0:
            inputData.turnLeftRadians = aimState.mouseSensibility * Math.abs(mouse.dx)
        elif mouse.dx > 0:
            inputData.turnRightRadians = aimState.mouseSensibility * Math.abs(mouse.dx)

        if mouse.dy < 0:
            inputData.lookUpRadians = aimState.mouseSensibility * Math.abs(mouse.dy)
        elif mouse.dy > 0:
            inputData.lookDownRadians = aimState.mouseSensibility * Math.abs(mouse.dy)

        if mouse.isLeftButtonPressed():
            inputData.fire = True

        if mouse.isRightButtonClicked() and type(self.gameData.playerItems.currentWeapon) == Sniper:
            self.aimStateSwitcher.switchDefaultOrSniper()

        if mouse.getScrollDelta() != 0 and type(aimState) == SniperAimState:
            if mouse.getScrollDelta() > 0:
                aimState.zoomIn()
            elif mouse.getScrollDelta() < 0:
                aimState.zoomOut()


def makePlayerInputManager(resolver):
    return PlayerInputManager(
        resolver.resolve(GameData), resolver.resolve(InputManager), resolver.resolve(AimStateSwitcher), resolver.resolve(EventManager)
    )
