from game.engine.weapon.WeaponFireLogic import WeaponFireLogic


class WeaponFireUpdater:

    def __init__(
        self,
        weaponFireLogic: WeaponFireLogic,
    ):
        self.weaponFireLogic = weaponFireLogic

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState, gameState.player, gameState.playerInputData)

    def updateForEnemies(self, gameState):
        for enemy, inputData in gameState.enemyInputData.items():
            self.updateForPerson(gameState, enemy, inputData)

    def updateForPerson(self, gameState, person, inputData):
        personItems = gameState.allPersonItems[person]

        # reset firing before process fire
        personItems.rightHandWeapon.isFiring = False
        if personItems.leftHandWeapon is not None:
            personItems.leftHandWeapon.isFiring = False

        if inputData.fire and (not inputData.altFire or personItems.currentWeapon.allowFireWithAltFire):
            self.weaponFireLogic.fireCurrentWeapon(person, personItems)
