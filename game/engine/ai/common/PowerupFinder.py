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

    def tryFindNearestHealthOrVest(self, bot, powerups, collisionTree):
        healthes = self.getNearestPowerups(bot, powerups, lambda x: type(x) == SmallHealthPowerup or type(x) == LargeHealthPowerup)
        for health in healthes:
            bot.aiData.route = self.routeFinder.getRoute(bot.currentCenterPoint, health.pickupPosition, collisionTree)
            if bot.aiData.route.hasPoints():
                return True

        vests = self.getNearestPowerups(bot, powerups, lambda x: type(x) == VestPowerup)
        for vest in vests:
            bot.aiData.route = self.routeFinder.getRoute(bot.currentCenterPoint, vest.pickupPosition, collisionTree)
            if bot.aiData.route.hasPoints():
                return True

        return False

    def tryFindNearestWeapon(self, bot, powerups, collisionTree):
        weapons = self.getNearestPowerups(bot, powerups, lambda x: type(x) == WeaponPowerup)
        for weapon in weapons:
            bot.aiData.route = self.routeFinder.getRoute(bot.currentCenterPoint, weapon.pickupPosition, collisionTree)
            if bot.aiData.route.hasPoints():
                return True

        return False

    def getNearestPowerups(self, bot, powerups, conditionFunc):
        return Query(powerups).where(conditionFunc).orderBy(lambda x: x.pickupPosition.getLengthTo(bot.currentCenterPoint)).result
