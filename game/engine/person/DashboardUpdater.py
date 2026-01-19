from game.model.weapon.NullWeapon import NullWeapon


class DashboardUpdater:

    def update(self, gameState):
        player = gameState.player
        playerItems = gameState.playerItems
        dashboard = gameState.dashboard

        # set current values
        dashboard.health = player.health
        dashboard.vest = playerItems.vest
        dashboard.bulletsCount = playerItems.getLeftRightWeaponBulletsCount()
        dashboard.maxBulletsCount = playerItems.getLeftRightWeaponMaxBulletsCount()
        dashboard.selectedWeaponType = type(playerItems.selectedCurrentWeapon or playerItems.currentWeapon)
        dashboard.weaponTypesSet = playerItems.getNonemptyWeaponTypesSet()
        dashboard.fragStatisticSet = set(gameState.personFragStatistic.values())

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
            self.updateStringData(gameState, dashboard, playerItems)

    def updateStringData(self, gameState, dashboard, playerItems):
        dashboard.healthStr = self.getAlignedNumber(dashboard.health)
        dashboard.vestStr = self.getAlignedNumber(dashboard.vest)
        if playerItems.currentWeapon != NullWeapon.instance:
            dashboard.bulletsCountStr = self.getAlignedNumber(f"{self.getAlignedNumber(dashboard.bulletsCount)}/{dashboard.maxBulletsCount}")
        else:
            dashboard.bulletsCountStr = ""
        dashboard.fragStatisticStr = []
        stat = gameState.personFragStatistic[gameState.player]
        dashboard.fragStatisticStr.append(("player", str(stat.frags), str(stat.deaths)))
        for index, enemy in enumerate(gameState.enemies):
            stat = gameState.personFragStatistic[enemy]
            dashboard.fragStatisticStr.append((f"enemy{index+1}", str(stat.frags), str(stat.deaths)))

    def getAlignedNumber(self, number):
        return str(number).rjust(3)
