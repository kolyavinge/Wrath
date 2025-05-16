from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.weapon.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager


class WeaponFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        weaponFeedbackLogic: WeaponFeedbackLogic,
        weaponSelector: WeaponSelector,
        traversal: BSPTreeTraversal,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.weaponSelector = weaponSelector
        self.traversal = traversal
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
        if weapon.bulletsCount == 0:
            personItems.removeWeaponByType(type(weapon))
            self.weaponSelector.selectNextWeapon(person, weapon)

        weapon.delayRemain = weapon.delay
        self.weaponFeedbackLogic.applyFeedback(weapon)

        bullet = weapon.makeBullet(person)
        self.gameData.bullets.append(bullet)
        bullet.currentLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, bullet.currentPosition)
        bullet.nextLevelSegment = bullet.currentLevelSegment

        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, bullet.currentPosition)
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
