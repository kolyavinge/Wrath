from game.engine.GameState import GameState
from game.input.InputManager import InputManager
from game.input.Keyboard import KeyboardButtons
from game.input.Mouse import MouseButtons
from game.lib.EventManager import EventManager, Events
from game.lib.Math import Math
from game.model.person.AimState import DefaultAimState, SniperAimState
from game.model.person.PersonStates import LifeCycle


class PlayerInputManager:

    def __init__(
        self,
        gameState: GameState,
        inputManager: InputManager,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.inputManager = inputManager
        self.eventManager = eventManager

    def processInput(self):
        self.gameState.playerInputData.clear()
        player = self.gameState.player
        if player.lifeCycle != LifeCycle.alive or player.isParalyzed():
            return
        self.processKeyboard()
        self.processMouse()

    def processKeyboard(self):
        inputData = self.gameState.playerInputData
        keyboard = self.inputManager.keyboard

        if keyboard.isPressed(KeyboardButtons.d1):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 1))
        elif keyboard.isPressed(KeyboardButtons.d2):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 2))
        elif keyboard.isPressed(KeyboardButtons.d3):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 3))
        elif keyboard.isPressed(KeyboardButtons.d4):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 4))
        elif keyboard.isPressed(KeyboardButtons.d5):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 5))
        elif keyboard.isPressed(KeyboardButtons.d6):
            self.eventManager.raiseEvent(Events.selectWeaponRequested, (self.gameState.player, 6))

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
        inputData = self.gameState.playerInputData
        mouse = self.inputManager.mouse
        aimState = self.gameState.aimState

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

        if mouse.isPressedOrHeld(MouseButtons.right):
            inputData.altFire = True

        if mouse.scrollDelta != 0:
            if type(aimState) == DefaultAimState:
                if mouse.scrollDelta > 0:
                    self.eventManager.raiseEvent(Events.selectNextWeaponRequested, self.gameState.player)
                elif mouse.scrollDelta < 0:
                    self.eventManager.raiseEvent(Events.selectPrevWeaponRequested, self.gameState.player)
            elif type(aimState) == SniperAimState:
                if mouse.scrollDelta > 0:
                    aimState.zoomIn()
                elif mouse.scrollDelta < 0:
                    aimState.zoomOut()
