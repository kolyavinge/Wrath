class Dashboard:

    def __init__(self):
        # last values
        self.lastHealth = 0
        self.lastVest = 0
        self.lastBulletsCount = 0
        self.lastMaxBulletsCount = 0
        self.lastSelectedWeaponType = None
        self.lastWeaponTypesSet = set()
        self.lastFragStatisticSet = set()

        # current values
        self.health = self.lastHealth
        self.vest = self.lastVest
        self.bulletsCount = self.lastBulletsCount
        self.maxBulletsCount = self.lastMaxBulletsCount
        self.selectedWeaponType = self.lastSelectedWeaponType
        self.weaponTypesSet = self.lastWeaponTypesSet
        self.fragStatisticSet = self.lastFragStatisticSet

        self.hasChanged = False

        self.healthStr = ""
        self.vestStr = ""
        self.bulletsCountStr = ""
        self.fragStatisticStr = []

    def resetChanges(self):
        self.lastHealth = self.health
        self.lastVest = self.vest
        self.lastBulletsCount = self.bulletsCount
        self.lastMaxBulletsCount = self.maxBulletsCount
        self.lastSelectedWeaponType = self.selectedWeaponType
        self.lastWeaponTypesSet = self.weaponTypesSet
        self.lastFragStatisticSet = self.fragStatisticSet
