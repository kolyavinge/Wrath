from game.anx.Events import Events
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager


class TorchSwitcher:

    def __init__(self, gameData, eventManager):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        if self.gameData.playerInputData.torchSwitch:
            self.gameData.playerInputData.torchSwitch = False
            self.gameData.playerItems.torch.switch()
            self.eventManager.raiseEvent(Events.torchSwitched)


def makeTorchSwitcher(resolver):
    return TorchSwitcher(resolver.resolve(GameData), resolver.resolve(EventManager))
