from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager


class WeaponFireLogic:

    def __init__(self, gameData, traversal, eventManager):
        self.gameData = gameData
        self.traversal = traversal
        self.eventManager = eventManager

    def process(self):
        weapon = self.gameData.playerItems.currentWeapon
        self.processWeapon(weapon)

    def processWeapon(self, weapon):
        weapon.isFiring = False
        if weapon.delayRemain > 0:
            weapon.delayRemain -= 1
        if self.gameData.playerInputData.fire:
            self.fire(weapon)

    def fire(self, weapon):
        if weapon.bulletsCount > 0 and weapon.delayRemain == 0:
            weapon.isFiring = True
            weapon.bulletsCount -= 1
            weapon.delayRemain = weapon.delay
            bullet = weapon.makeBullet()
            bspTree = self.gameData.level.collisionTree
            bullet.levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            self.gameData.bullets.append(bullet)
            self.eventManager.raiseEvent(Events.weaponFired, weapon)


def makeWeaponFireLogic(resolver):
    return WeaponFireLogic(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal), resolver.resolve(EventManager))
