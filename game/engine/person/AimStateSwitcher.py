from game.engine.GameState import GameState
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.lib.EventManager import EventManager, Events
from game.model.person.AimState import DefaultAimState, SniperAimState


class AimStateSwitcher:

    def __init__(
        self,
        gameData: GameState,
        weaponPositionUpdater: PersonWeaponPositionUpdater,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.weaponPositionUpdater = weaponPositionUpdater
        self.eventManager = eventManager

    def setToDefaultIfNeeded(self):
        if type(self.gameData.aimState) != DefaultAimState:
            self.gameData.aimState = DefaultAimState()
            self.gameData.playerItems.currentWeapon.setPositionForDefaultAimState()
            self.updatePlayerWeaponPosition()
            self.eventManager.raiseEvent(Events.aimStateSwitched, self.gameData.aimState)

    def switchDefaultOrSniper(self):
        if type(self.gameData.aimState) == DefaultAimState:
            self.gameData.aimState = SniperAimState()
            self.gameData.playerItems.currentWeapon.setPositionForSniperAimState()
        else:
            self.gameData.aimState = DefaultAimState()
            self.gameData.playerItems.currentWeapon.setPositionForDefaultAimState()
        self.updatePlayerWeaponPosition()
        self.eventManager.raiseEvent(Events.aimStateSwitched, self.gameData.aimState)

    def updatePlayerWeaponPosition(self):
        # обновляем позицию оружия сразу, не дожидаясь след цикла апдейта
        # иначе оружие может отрендерится на старой позиции
        self.weaponPositionUpdater.updateForPerson(self.gameData.player)
