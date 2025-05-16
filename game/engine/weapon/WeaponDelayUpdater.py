from game.engine.GameData import GameData


class WeaponDelayUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for personItems in self.gameData.allPersonItems.values():
            self.updateWeapon(personItems, personItems.currentWeapon)

    def updateWeapon(self, personItems, weapon):
        if weapon.delayRemain > 0:
            weapon.delayRemain -= 1
            if weapon.delayRemain == 0:
                personItems.switchTwoHandedWeaponIfNeeded()
