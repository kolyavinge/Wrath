from game.anx.Events import Events
from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Random import Random


class WeaponFireLogic:

    def __init__(self, gameData, traversal, eventManager):
        self.gameData = gameData
        self.traversal = traversal
        self.eventManager = eventManager
        self.rand = Random()

    def process(self):
        weapon = self.gameData.playerItems.currentWeapon
        self.processWeapon(self.gameData.player, weapon)

    def processWeapon(self, person, weapon):
        weapon.isFiring = False
        if weapon.delayRemain > 0:
            weapon.delayRemain -= 1
        if self.gameData.playerInputData.fire:
            if self.fire(weapon):
                self.eventManager.raiseEvent(Events.weaponFired, (person, weapon))

    def fire(self, weapon):
        if weapon.bulletsCount > 0 and weapon.delayRemain == 0:
            weapon.isFiring = True
            weapon.bulletsCount -= 1
            weapon.delayRemain = weapon.delay
            newJitter = self.getNewJitter(weapon)
            newFeedback = self.getNewFeedback(newJitter, weapon)
            weapon.jitter.add(newJitter)
            weapon.feedback.add(newFeedback)

            bullet = weapon.makeBullet()
            bspTree = self.gameData.level.collisionTree
            bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            self.gameData.bullets.append(bullet)

            bspTree = self.gameData.level.visibilityTree
            flashLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, weapon.position)
            if flashLevelSegment in self.gameData.visibleLevelSegments:
                flash = weapon.makeFlash()
                flashLevelSegment.weaponFlashes.append(flash)

            return True
        else:
            return False

    def getNewJitter(self, weapon):
        x = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)
        y = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)
        z = self.rand.getFloat(-weapon.jitterDelta, weapon.jitterDelta)

        return Vector3(x, y, z)

    def getNewFeedback(self, newJitter, weapon):
        newFeedback = weapon.direction.copy()
        newFeedback.add(newJitter)
        newFeedback.setLength(weapon.feedbackLength)
        newFeedback.mul(-1)

        return newFeedback


def makeWeaponFireLogic(resolver):
    return WeaponFireLogic(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal), resolver.resolve(EventManager))
