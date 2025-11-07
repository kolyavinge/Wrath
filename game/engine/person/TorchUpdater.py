from game.engine.GameData import GameData
from game.lib.EventManager import EventManager, Events


class TorchUpdater:

    def __init__(
        self,
        gameData: GameData,
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
