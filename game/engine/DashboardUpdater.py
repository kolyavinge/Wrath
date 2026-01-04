from game.engine.GameState import GameState
from game.model.weapon.NullWeapon import NullWeapon


class DashboardUpdater:

    def __init__(self, gameData: GameState):
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
        dashboard.weaponTypesSet = playerItems.getNonemptyWeaponTypesSet()
        dashboard.fragStatisticSet = set(self.gameData.personFragStatistic.values())

        # check for changes
        dashboard.hasChanged = (
            dashboard.lastHealth != dashboard.health
            or dashboard.lastVest != dashboard.vest
            or dashboard.lastBulletsCount != dashboard.bulletsCount
            or dashboard.lastMaxBulletsCount != dashboard.maxBulletsCount
            or dashboard.lastSelectedWeaponType != dashboard.selectedWeaponType
            or dashboard.lastWeaponTypesSet != dashboard.weaponTypesSet
            or dashboard.lastFragStatisticSet != dashboard.fragStatisticSet
        )

        if dashboard.hasChanged:
            self.updateStringData(dashboard, playerItems)

    def updateStringData(self, dashboard, playerItems):
        dashboard.healthStr = self.getAlignedNumber(dashboard.health)
        dashboard.vestStr = self.getAlignedNumber(dashboard.vest)
        if playerItems.currentWeapon != NullWeapon.instance:
            dashboard.bulletsCountStr = self.getAlignedNumber(f"{self.getAlignedNumber(dashboard.bulletsCount)}/{dashboard.maxBulletsCount}")
        else:
            dashboard.bulletsCountStr = ""
        dashboard.fragStatisticStr = []
        stat = self.gameData.personFragStatistic[self.gameData.player]
        dashboard.fragStatisticStr.append(("player", str(stat.frags), str(stat.deaths)))
        for index, enemy in enumerate(self.gameData.enemies):
            stat = self.gameData.personFragStatistic[enemy]
            dashboard.fragStatisticStr.append((f"enemy{index+1}", str(stat.frags), str(stat.deaths)))

    def getAlignedNumber(self, number):
        return str(number).rjust(3)
