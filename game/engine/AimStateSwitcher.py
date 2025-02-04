from game.engine.GameData import GameData
from game.model.AimState import DefaultAimState, SniperAimState


class AimStateSwitcher:

    def __init__(self, gameData):
        self.gameData = gameData

    def setToDefaultIfNeeded(self):
        if type(self.gameData.aimState) != DefaultAimState:
            self.gameData.aimState = DefaultAimState()

    def switchDefaultOrSniper(self):
        if type(self.gameData.aimState) == DefaultAimState:
            self.gameData.aimState = SniperAimState()
        else:
            self.gameData.aimState = DefaultAimState()


def makeAimStateSwitcher(resolver):
    return AimStateSwitcher(resolver.resolve(GameData))
