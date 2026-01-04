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
        player = self.gameState.player
        torch = self.gameState.playerTorch
        torch.position = player.eyePosition
        torch.direction = player.lookDirection

    def switchTorch(self, _):
        torch = self.gameState.playerTorch
        torch.switch()
        self.eventManager.raiseEvent(Events.torchSwitched)
