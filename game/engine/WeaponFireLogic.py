from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.lib.EventManager import EventManager


class WeaponFireLogic:

    def __init__(self, gameData, weaponFeedbackLogic, traversal, eventManager):
        self.gameData = gameData
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.traversal = traversal
        self.eventManager = eventManager

    def process(self):
        personItems = self.gameData.playerItems
        weapon = personItems.currentWeapon
        self.processWeapon(self.gameData.player, weapon)

    def processWeapon(self, person, weapon):
        if self.gameData.playerInputData.fire:  # TODO person input data
            if self.canFire(weapon):
                self.fire(weapon)
                self.eventManager.raiseEvent(Events.weaponFired, (person, weapon))

    def canFire(self, weapon):
        return weapon.bulletsCount > 0 and weapon.delayRemain == 0

    def fire(self, weapon):
        weapon.bulletsCount -= 1
        weapon.delayRemain = weapon.delay
        self.weaponFeedbackLogic.applyFeedback(weapon)

        bullet = weapon.makeBullet()
        self.gameData.bullets.append(bullet)
        bspTree = self.gameData.level.collisionTree
        bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)

        bspTree = self.gameData.level.visibilityTree
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment = visibilityLevelSegment
            visibilityLevelSegment.bullets.append(bullet)

        if visibilityLevelSegment in self.gameData.visibleLevelSegments:
            flash = weapon.makeFlash()
            if flash is not None:
                visibilityLevelSegment.weaponFlashes.append(flash)

        trace = bullet.makeTrace()
        if trace is not None:
            self.gameData.bulletTraces.append(trace)
            visibilityLevelSegment.bulletTraces.append(trace)
            trace.visibilityLevelSegments.add(visibilityLevelSegment)


def makeWeaponFireLogic(resolver):
    return WeaponFireLogic(
        resolver.resolve(GameData), resolver.resolve(WeaponFeedbackLogic), resolver.resolve(BSPTreeTraversal), resolver.resolve(EventManager)
    )
