from game.anx.Events import Events
from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.List import List
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupCollisionProcessor:

    def __init__(self, gameData, powerupCollisionDetector, eventManager):
        self.gameData = gameData
        self.powerupCollisionDetector = powerupCollisionDetector
        self.eventManager = eventManager
        self.actions = {}
        self.actions[WeaponPowerup] = self.processWeaponPowerup
        self.actions[LargeHealthPowerup] = self.processHealthPowerup
        self.actions[SmallHealthPowerup] = self.processHealthPowerup

    def process(self):
        self.processPerson(self.gameData.player)

    def processPerson(self, person):
        powerup = self.powerupCollisionDetector.getCollisionResultOrNone(person)
        if powerup is not None:
            self.actions[type(powerup)](person, powerup)
            self.gameData.powerups.remove(powerup)
            powerup.collisionLevelSegment.powerups.remove(powerup)
            powerup.visibilityLevelSegment.powerups.remove(powerup)
            self.eventManager.raiseEvent(Events.powerupPickedUp, (person, powerup))

    def processWeaponPowerup(self, person, powerup):
        weapons = self.gameData.allPersonItems[person].weapons
        weapon = List.firstOrNone(lambda w: type(w) == powerup.weaponType, weapons)
        if weapon is not None:
            weapon.addBullets(weapon.maxBulletsCount)
        else:
            weapons.add(powerup.weaponType())

    def processHealthPowerup(self, person, powerup):
        person.addHealth(powerup.value)


def makePowerupCollisionProcessor(resolver):
    return PowerupCollisionProcessor(resolver.resolve(GameData), resolver.resolve(PowerupCollisionDetector), resolver.resolve(EventManager))
