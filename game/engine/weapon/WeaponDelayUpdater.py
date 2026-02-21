class WeaponDelayUpdater:

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerItems, gameState.updateStatistic)

    def updateForBots(self, gameState):
        for bot, botItems in gameState.botItems.items():
            self.updateForPerson(bot, botItems, gameState.updateStatistic)

    def updateForPerson(self, person, personItems, updateStatistic):
        self.updateWeapon(person, personItems, personItems.rightHandWeapon, updateStatistic)
        if personItems.leftHandWeapon is not None:
            self.updateWeapon(person, personItems, personItems.leftHandWeapon, updateStatistic)

    def updateWeapon(self, person, personItems, weapon, updateStatistic):
        if not weapon.delayRemain.isExpired():
            weapon.delayRemain.decrease()
            if weapon.delayRemain.isExpired():
                personItems.switchTwoHandedWeaponIfNeeded()

        if weapon.needReload and not weapon.reloadDelayRemain.isExpired():
            weapon.reloadDelayRemain.decrease()
            if weapon.reloadDelayRemain.isExpired():
                updateStatistic.reloadedWeapons.append((person, weapon))
