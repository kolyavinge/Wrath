from game.engine.GameData import GameData
from game.lib.List import List
from game.model.weapon.NullWeapon import NullWeapon


class DashboardUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        playerItems = self.gameData.playerItems
        dashboard = self.gameData.dashboard

        # set current values
        dashboard.health = player.health
        dashboard.vest = playerItems.vest
        dashboard.bulletsCount = playerItems.getLeftRightWeaponBulletsCount()
        dashboard.maxBulletsCount = playerItems.getLeftRightWeaponMaxBulletsCount()
        dashboard.selectedWeaponType = type(playerItems.selectedCurrentWeapon or playerItems.currentWeapon)
        dashboard.weaponTypes = playerItems.getNonemptyWeaponTypes()

        # check for changes
        dashboard.hasChanged = (
            dashboard.lastHealth != dashboard.health
            or dashboard.lastVest != dashboard.vest
            or dashboard.lastBulletsCount != dashboard.bulletsCount
            or dashboard.lastMaxBulletsCount != dashboard.maxBulletsCount
            or dashboard.lastSelectedWeaponType != dashboard.selectedWeaponType
            or not List.equals(dashboard.lastWeaponTypes, dashboard.weaponTypes)
        )

        if dashboard.hasChanged:
            dashboard.healthStr = self.getAlignedNumber(dashboard.health)
            dashboard.vestStr = self.getAlignedNumber(dashboard.vest)
            if playerItems.currentWeapon != NullWeapon.instance:
                dashboard.bulletsCountStr = self.getAlignedNumber(f"{self.getAlignedNumber(dashboard.bulletsCount)}/{dashboard.maxBulletsCount}")
            else:
                dashboard.bulletsCountStr = ""

    def getAlignedNumber(self, number):
        return str(number).rjust(3)
