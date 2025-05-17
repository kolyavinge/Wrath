from game.anx.Events import Events
from game.engine.GameData import GameData
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager


class WeaponFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        weaponFeedbackLogic: WeaponFeedbackLogic,
        bulletLogic: BulletLogic,
        weaponSelector: WeaponSelector,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.bulletLogic = bulletLogic
        self.weaponSelector = weaponSelector
        self.eventManager = eventManager

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            personItems = self.gameData.allPersonItems[person]
            self.updateForWeapon(person, personItems, inputData)

    def updateForWeapon(self, person, personItems, inputData):
        weapon = personItems.currentWeapon
        if inputData.fire and self.canFire(weapon):
            weapon.isFiring = True
            self.fire(person, personItems, weapon)
            self.eventManager.raiseEvent(Events.weaponFired, (person, weapon))
        else:
            weapon.isFiring = False

    def canFire(self, weapon):
        return weapon.bulletsCount > 0 and weapon.delayRemain == 0

    def fire(self, person, personItems, weapon):
        weapon.bulletsCount -= 1
        weapon.delayRemain = weapon.delay
        self.weaponFeedbackLogic.applyFeedback(weapon)
        self.bulletLogic.makeBullet(person, weapon)
        self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems, weapon)
