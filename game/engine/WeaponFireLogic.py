from game.anx.Events import Events
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager


class WeaponFireLogic:

    def __init__(self, gameData, eventManager):
        self.gameData = gameData
        self.eventManager = eventManager

    def process(self):
        weapon = self.gameData.playerItems.currentWeapon
        weapon.isFiring = False
        if self.gameData.playerInputData.fire:
            self.fire(weapon)

    def fire(self, weapon):
        if weapon.bulletsCount > 0:
            weapon.isFiring = True
            weapon.bulletsCount -= 1
            bullet = weapon.makeBullet()
            self.gameData.bullets.append(bullet)
            self.eventManager.raiseEvent(Events.weaponFired, weapon)


def makeWeaponFireLogic(resolver):
    return WeaponFireLogic(resolver.resolve(GameData), resolver.resolve(EventManager))
