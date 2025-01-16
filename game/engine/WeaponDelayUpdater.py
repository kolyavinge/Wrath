from game.engine.GameData import GameData


class WeaponDelayUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        personItems = self.gameData.playerItems
        weapon = personItems.currentWeapon
        self.updateWeapon(personItems, weapon)

    def updateWeapon(self, personItems, weapon):
        if weapon.delayRemain > 0:
            weapon.delayRemain -= 1
            if weapon.delayRemain == 0:
                self.switchTwoHandedWeaponIfNeeded(personItems)

    def switchTwoHandedWeaponIfNeeded(self, personItems):
        if personItems.leftHandWeapon is not None:
            if personItems.rightHandWeapon == personItems.currentWeapon:
                personItems.currentWeapon = personItems.leftHandWeapon
            else:
                personItems.currentWeapon = personItems.rightHandWeapon


def makeWeaponDelayUpdater(resolver):
    return WeaponDelayUpdater(resolver.resolve(GameData))
