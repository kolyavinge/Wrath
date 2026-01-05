from game.engine.GameState import GameState
from game.lib.EventManager import EventManager, Events


class TorchUpdater:

    def __init__(
        self,
        gameState: GameState,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.eventManager = eventManager
        self.eventManager.attachToEvent(Events.torchSwitchRequested, self.switchTorch)

    def update(self):
        torch = self.gameState.playerItems.torch
        torch.position = self.gameState.player.eyePosition
        torch.direction = self.gameState.player.lookDirection

    def switchTorch(self, _):
        torch = self.gameState.playerItems.torch
        torch.switch()
        self.eventManager.raiseEvent(Events.torchSwitched)
