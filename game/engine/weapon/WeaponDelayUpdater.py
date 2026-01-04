from game.engine.GameState import GameState
from game.lib.EventManager import EventManager, Events


class WeaponDelayUpdater:

    def __init__(
        self,
        gameData: GameState,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        for person, personItems in self.gameData.allPersonItems.items():
            self.updateWeapon(person, personItems, personItems.rightHandWeapon)
            if personItems.leftHandWeapon is not None:
                self.updateWeapon(person, personItems, personItems.leftHandWeapon)

    def updateWeapon(self, person, personItems, weapon):
        if not weapon.delayRemain.isExpired():
            weapon.delayRemain.decrease()
            if weapon.delayRemain.isExpired():
                personItems.switchTwoHandedWeaponIfNeeded()

        if weapon.needReload and not weapon.reloadDelayRemain.isExpired():
            weapon.reloadDelayRemain.decrease()
            if weapon.reloadDelayRemain.isExpired():
                self.eventManager.raiseEvent(Events.weaponReloaded, (person, weapon))
