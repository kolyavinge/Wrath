from game.lib.EventManager import EventManager, Events


class WeaponDelayUpdater:

    def __init__(
        self,
        eventManager: EventManager,
    ):
        self.eventManager = eventManager

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerItems)

    def updateForEnemies(self, gameState):
        for enemy, enemyItems in gameState.enemyItems.items():
            self.updateForPerson(enemy, enemyItems)

    def updateForPerson(self, person, personItems):
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
