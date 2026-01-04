from game.engine.GameState import GameState
from game.lib.EventManager import EventManager, Events


class TorchUpdater:

    def __init__(
        self,
        gameData: GameState,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager
        self.eventManager.attachToEvent(Events.torchSwitchRequested, self.switchTorch)

    def update(self):
        player = self.gameData.player
        torch = self.gameData.playerTorch
        torch.position = player.eyePosition
        torch.direction = player.lookDirection

    def switchTorch(self, _):
        torch = self.gameData.playerTorch
        torch.switch()
        self.eventManager.raiseEvent(Events.torchSwitched)
