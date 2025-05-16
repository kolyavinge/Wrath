from game.anx.Events import Events
from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.GameData import GameData
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        powerupCollisionDetector: PowerupCollisionDetector,
        weaponSelector: WeaponSelector,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.powerupCollisionDetector = powerupCollisionDetector
        self.weaponSelector = weaponSelector
        self.eventManager = eventManager
        self.actions = {}
        self.actions[WeaponPowerup] = self.processWeaponPowerup
        self.actions[LargeHealthPowerup] = self.processHealthPowerup
        self.actions[SmallHealthPowerup] = self.processHealthPowerup
        self.actions[VestPowerup] = self.processVestPowerup

    def update(self):
        for person in self.gameData.allPerson:
            self.updateForPerson(person)

    def updateForPerson(self, person):
        powerup = self.powerupCollisionDetector.getCollisionResultOrNone(person)
        if powerup is not None:
            self.actions[type(powerup)](person, powerup)
            self.gameData.powerups.remove(powerup)
            powerup.collisionLevelSegment.powerups.remove(powerup)
            powerup.visibilityLevelSegment.powerups.remove(powerup)
            self.eventManager.raiseEvent(Events.powerupPickedUp, (person, powerup))

    def processWeaponPowerup(self, person, powerup):
        personItems = self.gameData.allPersonItems[person]
        findedWeapons = personItems.getWeaponsByType(powerup.weaponType)
        if len(findedWeapons) > 0:
            for findedWeapon in findedWeapons:
                findedWeapon.addBullets(findedWeapon.maxBulletsCount)
        else:
            selectThisWeapon = not personItems.hasWeapons()
            for _ in range(0, powerup.count):
                personItems.weapons.add(powerup.weaponType())
            if selectThisWeapon:
                self.weaponSelector.selectWeaponByType(person, powerup.weaponType)

    def processHealthPowerup(self, person, powerup):
        person.addHealth(powerup.value)

    def processVestPowerup(self, person, powerup):
        self.gameData.allPersonItems[person].setFullVest()
