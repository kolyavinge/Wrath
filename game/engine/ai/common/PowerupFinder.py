from game.engine.ai.common.RouteFinder import RouteFinder
from game.engine.GameState import GameState
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupFinder:

    def __init__(
        self,
        gameData: GameState,
        routeFinder: RouteFinder,
    ):
        self.gameData = gameData
        self.routeFinder = routeFinder

    def tryFindNearestHealthOrVest(self, enemy):
        healthes = self.getNearestPowerups(enemy, lambda x: type(x) == SmallHealthPowerup or type(x) == LargeHealthPowerup)
        for health in healthes:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, health.pickupPosition)
            if enemy.aiData.route.hasPoints():
                return True

        vests = self.getNearestPowerups(enemy, lambda x: type(x) == VestPowerup)
        for vest in vests:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, vest.pickupPosition)
            if enemy.aiData.route.hasPoints():
                return True

        return False

    def tryFindNearestWeapon(self, enemy):
        weapons = self.getNearestPowerups(enemy, lambda x: type(x) == WeaponPowerup)
        for weapon in weapons:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, weapon.pickupPosition)
            if enemy.aiData.route.hasPoints():
                return True

        return False

    def getNearestPowerups(self, enemy, conditionFunc):
        return Query(self.gameData.powerups).where(conditionFunc).orderBy(lambda x: x.pickupPosition.getLengthTo(enemy.currentCenterPoint)).result
