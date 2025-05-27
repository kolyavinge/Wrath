from game.engine.ai.common.RouteFinder import RouteFinder
from game.engine.GameData import GameData
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup


class PowerupFinder:

    def __init__(
        self,
        gameData: GameData,
        routeFinder: RouteFinder,
    ):
        self.gameData = gameData
        self.routeFinder = routeFinder

    def tryFindNearestHealthOrVest(self, enemy):
        healthes = (
            Query(self.gameData.powerups)
            .where(lambda x: isinstance(x, SmallHealthPowerup) or isinstance(x, LargeHealthPowerup))
            .orderBy(lambda x: x.pickupPosition.getLengthTo(enemy.currentCenterPoint))
            .result
        )

        for health in healthes:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, health.pickupPosition)
            if enemy.aiData.route.hasPoints():
                return True

        vests = (
            Query(self.gameData.powerups)
            .where(lambda x: isinstance(x, VestPowerup))
            .orderBy(lambda x: x.pickupPosition.getLengthTo(enemy.currentCenterPoint))
            .result
        )

        for vest in vests:
            enemy.aiData.route = self.routeFinder.getRoute(enemy.currentCenterPoint, vest.pickupPosition)
            if enemy.aiData.route.hasPoints():
                return True

        return False
