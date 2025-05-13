from game.anx.Events import Events
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.person.AimState import DefaultAimState, SniperAimState


class AimStateSwitcher:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def setToDefaultIfNeeded(self):
        if type(self.gameData.aimState) != DefaultAimState:
            self.gameData.aimState = DefaultAimState()
            self.gameData.playerItems.currentWeapon.setPositionForDefaultAimState()
            self.eventManager.raiseEvent(Events.aimStateSwitched, self.gameData.aimState)

    def switchDefaultOrSniper(self):
        if type(self.gameData.aimState) == DefaultAimState:
            self.gameData.aimState = SniperAimState()
            self.gameData.playerItems.currentWeapon.setPositionForSniperAimState()
        else:
            self.gameData.aimState = DefaultAimState()
            self.gameData.playerItems.currentWeapon.setPositionForDefaultAimState()

        self.eventManager.raiseEvent(Events.aimStateSwitched, self.gameData.aimState)


def makeAimStateSwitcher(resolver):
    return AimStateSwitcher(
        resolver.resolve(GameData),
        resolver.resolve(EventManager),
    )
