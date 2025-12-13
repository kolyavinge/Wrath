from game.engine.GameData import GameData
from game.input.InputManager import InputManager
from game.input.Keyboard import KeyboardButtons
from game.input.Mouse import MouseButtons
from game.lib.EventManager import EventManager, Events
from game.lib.Math import Math
from game.model.person.AimState import DefaultAimState, SniperAimState
from game.model.person.PersonInputData import FireState
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

        if keyboard.isPressed(KeyboardButtons.d1):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 1))
        elif keyboard.isPressed(KeyboardButtons.d2):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 2))
        elif keyboard.isPressed(KeyboardButtons.d3):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 3))
        elif keyboard.isPressed(KeyboardButtons.d4):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 4))
        elif keyboard.isPressed(KeyboardButtons.d5):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 5))
        elif keyboard.isPressed(KeyboardButtons.d6):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameData.player, 6))

        if keyboard.isPressedOrHeld(KeyboardButtons.w):
            inputData.goForward = True
        elif keyboard.isPressedOrHeld(KeyboardButtons.s):
            inputData.goBackward = True

        if keyboard.isPressedOrHeld(KeyboardButtons.a):
            inputData.stepLeft = True
        elif keyboard.isPressedOrHeld(KeyboardButtons.d):
            inputData.stepRight = True

        if keyboard.isPressedOrHeld(KeyboardButtons.space):
            inputData.jump = True

        if keyboard.isPressed(KeyboardButtons.f):
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

        if mouse.isPressedOrHeld(MouseButtons.left):
            inputData.fire = True

        if mouse.isPressed(MouseButtons.right):
            inputData.altFireState = FireState.activated
        elif mouse.isHeld(MouseButtons.right):
            inputData.altFireState = FireState.active
        elif mouse.isLifted(MouseButtons.right):
            inputData.altFireState = FireState.deactivated

        if mouse.scrollDelta != 0:
            if type(aimState) == DefaultAimState:
                if mouse.scrollDelta > 0:
                    self.eventManager.raiseEvent(Events.selectNextWeaponRequested, self.gameData.player)
                elif mouse.scrollDelta < 0:
                    self.eventManager.raiseEvent(Events.selectPrevWeaponRequested, self.gameData.player)
            elif type(aimState) == SniperAimState:
                if mouse.scrollDelta > 0:
                    aimState.zoomIn()
                elif mouse.scrollDelta < 0:
                    aimState.zoomOut()
