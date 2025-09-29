from game.engine.GameData import GameData


class DashboardUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        playerItems = self.gameData.playerItems

        dashboard = self.gameData.dashboard
        dashboard.health = player.health
        dashboard.vest = playerItems.vest
        dashboard.bulletsCount = playerItems.getLeftRightWeaponBulletsCount()
        dashboard.maxBulletsCount = playerItems.getLeftRightWeaponMaxBulletsCount()

        dashboard.hasChanged = (
            dashboard.lastHealth != dashboard.health
            or dashboard.lastVest != dashboard.vest
            or dashboard.lastBulletsCount != dashboard.bulletsCount
            or dashboard.lastMaxBulletsCount != dashboard.maxBulletsCount
        )

        if dashboard.hasChanged:
            dashboard.healthStr = self.getAlignedNumber(dashboard.health)
            dashboard.vestStr = self.getAlignedNumber(dashboard.vest)
            dashboard.bulletsCountStr = self.getAlignedNumber(f"{self.getAlignedNumber(dashboard.bulletsCount)}/{dashboard.maxBulletsCount}")

    def getAlignedNumber(self, number):
        return str(number).rjust(3)
