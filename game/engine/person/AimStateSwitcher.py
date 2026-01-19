from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.lib.EventManager import EventManager, Events
from game.model.person.AimState import DefaultAimState, SniperAimState


class AimStateSwitcher:

    def __init__(
        self,
        weaponPositionUpdater: PersonWeaponPositionUpdater,
        eventManager: EventManager,
    ):
        self.weaponPositionUpdater = weaponPositionUpdater
        self.eventManager = eventManager

    def setToDefaultIfNeeded(self, player, playerItems):
        if type(player.aimState) != DefaultAimState:
            player.aimState = DefaultAimState()
            playerItems.currentWeapon.setPositionForDefaultAimState()
            self.updatePlayerWeaponPosition(player, playerItems)
            self.eventManager.raiseEvent(Events.aimStateSwitched, player)

    def switchDefaultOrSniper(self, player, playerItems):
        if type(player.aimState) == DefaultAimState:
            player.aimState = SniperAimState()
            playerItems.currentWeapon.setPositionForSniperAimState()
        else:
            player.aimState = DefaultAimState()
            playerItems.currentWeapon.setPositionForDefaultAimState()
        self.updatePlayerWeaponPosition(player, playerItems)
        self.eventManager.raiseEvent(Events.aimStateSwitched, player)

    def updatePlayerWeaponPosition(self, player, playerItems):
        # обновляем позицию оружия сразу, не дожидаясь след цикла апдейта
        # иначе оружие может отрендерится на старой позиции
        self.weaponPositionUpdater.updateForPerson(player, playerItems)
