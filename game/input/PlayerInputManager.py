from game.engine.GameData import GameData
from game.input.InputManager import InputManager
from game.input.Keys import Keys
from game.lib.EventManager import EventManager, Events
from game.lib.Math import Math
from game.model.person.AimState import DefaultAimState, SniperAimState
from game.model.person.PersonStates import LifeCycle


class PlayerInputManager:

    def __init__(
        self,
        gameData: GameData,
        inputManager: InputManager,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.inputManager = inputManager
        self.eventManager = eventManager

    def processInput(self):
        self.gameData.playerInputData.clear()
        player = self.gameData.player
        if player.lifeCycle != LifeCycle.alive or player.isParalyzed():
            return
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        inputData = self.gameData.playerInputData
        keyboard = self.inputManager.keyboard

        if keyboard.isPressed(Keys.d1):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 1))
        elif keyboard.isPressed(Keys.d2):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 2))
        elif keyboard.isPressed(Keys.d3):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 3))
        elif keyboard.isPressed(Keys.d4):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 4))
        elif keyboard.isPressed(Keys.d5):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 5))
        elif keyboard.isPressed(Keys.d6):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 6))

        if keyboard.isPressedOrHeld(Keys.w):
            inputData.goForward = True
        elif keyboard.isPressedOrHeld(Keys.s):
            inputData.goBackward = True

        if keyboard.isPressedOrHeld(Keys.a):
            inputData.stepLeft = True
        elif keyboard.isPressedOrHeld(Keys.d):
            inputData.stepRight = True

        if keyboard.isPressedOrHeld(Keys.space):
            inputData.jump = True

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

        if mouse.isRightButtonClicked():
            inputData.altFireClick = True

        if mouse.getScrollDelta() != 0:
            if type(aimState) == DefaultAimState:
                if mouse.getScrollDelta() > 0:
                    self.eventManager.raiseEvent(Events.selectNextWeaponRequested, self.gameData.player)
                elif mouse.getScrollDelta() < 0:
                    self.eventManager.raiseEvent(Events.selectPrevWeaponRequested, self.gameData.player)
            elif type(aimState) == SniperAimState:
                if mouse.getScrollDelta() > 0:
                    aimState.zoomIn()
                elif mouse.getScrollDelta() < 0:
                    aimState.zoomOut()
