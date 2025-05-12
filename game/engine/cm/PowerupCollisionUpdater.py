from game.anx.Events import Events
from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupCollisionUpdater:

    def __init__(self, gameData, powerupCollisionDetector, eventManager):
        self.gameData = gameData
        self.powerupCollisionDetector = powerupCollisionDetector
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
        personWeapons = self.gameData.allPersonItems[person].weapons
        findedWeapons = Query(personWeapons).where(lambda w: type(w) == powerup.weaponType).result
        if len(findedWeapons) > 0:
            for findedWeapon in findedWeapons:
                findedWeapon.addBullets(findedWeapon.maxBulletsCount)
        else:
            for _ in range(0, powerup.count):
                personWeapons.add(powerup.weaponType())

    def processHealthPowerup(self, person, powerup):
        person.addHealth(powerup.value)

    def processVestPowerup(self, person, powerup):
        self.gameData.allPersonItems[person].setFullVest()


def makePowerupCollisionUpdater(resolver):
    return PowerupCollisionUpdater(resolver.resolve(GameData), resolver.resolve(PowerupCollisionDetector), resolver.resolve(EventManager))
