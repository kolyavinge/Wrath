from game.lib.EventManager import EventManager, Events


class TorchUpdater:

    def __init__(
        self,
        eventManager: EventManager,
    ):
        self.eventManager = eventManager
        self.eventManager.attachToEvent(Events.torchSwitchRequested, self.switchTorch)

    def init(self, gameState):
        self.allPersonItems = gameState.allPersonItems

    def update(self, gameState):
        torch = gameState.playerItems.torch
        torch.position = gameState.player.eyePosition
        torch.direction = gameState.player.lookDirection

    def switchTorch(self, person):
        torch = self.allPersonItems[person].torch
        torch.switch()
        self.eventManager.raiseEvent(Events.torchSwitched)
