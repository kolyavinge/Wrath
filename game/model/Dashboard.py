class Dashboard:

    def __init__(self):
        # last values
        self.lastHealth = 0
        self.lastVest = 0
        self.lastBulletsCount = 0
        self.lastMaxBulletsCount = 0
        self.lastSelectedWeaponType = None
        self.lastWeaponTypes = []

        # current values
        self.health = 0
        self.vest = 0
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.selectedWeaponType = None
        self.weaponTypes = []

        self.hasChanged = False

        self.healthStr = ""
        self.vestStr = ""
        self.bulletsCountStr = ""

    def resetChanges(self):
        self.lastHealth = self.health
        self.lastVest = self.vest
        self.lastBulletsCount = self.bulletsCount
        self.lastMaxBulletsCount = self.maxBulletsCount
        self.lastSelectedWeaponType = self.selectedWeaponType
        self.lastWeaponTypes = self.weaponTypes
