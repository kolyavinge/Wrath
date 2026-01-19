from game.engine.GameState import GameState
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.lib.EventManager import EventManager, Events
from game.model.person.AimState import DefaultAimState, SniperAimState


class AimStateSwitcher:

    def __init__(
        self,
        gameState: GameState,
        weaponPositionUpdater: PersonWeaponPositionUpdater,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.weaponPositionUpdater = weaponPositionUpdater
        self.eventManager = eventManager

    def setToDefaultIfNeeded(self):
        if type(self.gameState.aimState) != DefaultAimState:
            self.gameState.aimState = DefaultAimState()
            self.gameState.playerItems.currentWeapon.setPositionForDefaultAimState()
            self.updatePlayerWeaponPosition()
            self.eventManager.raiseEvent(Events.aimStateSwitched, (self.gameState.player, self.gameState.aimState))

    def switchDefaultOrSniper(self):
        if type(self.gameState.aimState) == DefaultAimState:
            self.gameState.aimState = SniperAimState()
            self.gameState.playerItems.currentWeapon.setPositionForSniperAimState()
        else:
            self.gameState.aimState = DefaultAimState()
            self.gameState.playerItems.currentWeapon.setPositionForDefaultAimState()
        self.updatePlayerWeaponPosition()
        self.eventManager.raiseEvent(Events.aimStateSwitched, (self.gameState.player, self.gameState.aimState))

    def updatePlayerWeaponPosition(self):
        # обновляем позицию оружия сразу, не дожидаясь след цикла апдейта
        # иначе оружие может отрендерится на старой позиции
        self.weaponPositionUpdater.updateForPerson(self.gameState, self.gameState.player)
