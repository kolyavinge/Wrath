from game.lib.EventManager import EventManager, Events


class TorchUpdater:

    def __init__(
        self,
        eventManager: EventManager,
    ):
        eventManager.attachToEvent(Events.torchSwitchRequested, self.switchTorch)

    def update(self, gameState):
        torch = gameState.playerItems.torch
        torch.position = gameState.player.eyePosition
        torch.direction = gameState.player.lookDirection

    def switchTorch(self, torch):
        torch.switch()
