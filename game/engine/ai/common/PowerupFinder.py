from game.engine.ai.common.RouteFinder import RouteFinder
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupFinder:

    def __init__(
        self,
        routeFinder: RouteFinder,
    ):
        self.routeFinder = routeFinder

    def tryFindNearestHealthOrVest(self, enemy, powerups, collisionTree):
        healthes = self.getNearestPowerups(enemy, powerups, lambda x: type(x) == SmallHealthPowerup or type(x) == LargeHealthPowerup)
        for health in healthes:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, health.pickupPosition, collisionTree)
            if enemy.aiData.route.hasPoints():
                return True

        vests = self.getNearestPowerups(enemy, powerups, lambda x: type(x) == VestPowerup)
        for vest in vests:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, vest.pickupPosition, collisionTree)
            if enemy.aiData.route.hasPoints():
                return True

        return False

    def tryFindNearestWeapon(self, enemy, powerups, collisionTree):
        weapons = self.getNearestPowerups(enemy, powerups, lambda x: type(x) == WeaponPowerup)
        for weapon in weapons:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, weapon.pickupPosition, collisionTree)
            if enemy.aiData.route.hasPoints():
                return True

        return False

    def getNearestPowerups(self, enemy, powerups, conditionFunc):
        return Query(powerups).where(conditionFunc).orderBy(lambda x: x.pickupPosition.getLengthTo(enemy.currentCenterPoint)).result
