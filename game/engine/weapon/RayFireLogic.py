from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager, Events
from game.lib.Query import Query


class RayFireLogic:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        weaponSelector: WeaponSelector,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.weaponSelector = weaponSelector
        self.eventManager = eventManager

    def activateRay(self, person, weapon):
        ray = weapon.makeRay(person)
        ray.startLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, ray.startPosition)
        ray.endLevelSegment = ray.startLevelSegment
        ray.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, ray.startPosition)
        ray.visibilityLevelSegment.rays.append(ray)
        ray.initTimeSec = self.gameData.globalTimeSec
        self.gameData.rays.append(ray)
        self.eventManager.raiseEvent(Events.rayActivated, (person, weapon, ray))

    def fire(self, person, personItems):
        weapon = personItems.currentWeapon
        if self.canFire(person, weapon):
            weapon.isFiring = True
            if weapon.delayRemain.isExpired():
                weapon.bulletsCount -= 1
                weapon.delayRemain.set(weapon.delay)
                self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)

    def canFire(self, person, weapon):
        return person.weaponSelectState is None and weapon.bulletsCount > 0

    def deactivateRay(self, person, weapon):
        ray = Query(self.gameData.rays).first(lambda r: r.weapon == weapon)
        self.gameData.rays.remove(ray)
        ray.visibilityLevelSegment.rays.remove(ray)
        weapon.delayRemain.set(2 * weapon.delay)
        self.eventManager.raiseEvent(Events.rayDeactivated, (person, weapon, ray))
