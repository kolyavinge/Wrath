from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.ai.common.RouteFinder import RouteFinder
from game.engine.GameData import GameData
from game.lib.Query import Query
from game.lib.Random import Random
from game.model.ai.EnemyState import EnemyState
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup


class HealthSearchStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        routeFinder: RouteFinder,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.routeFinder = routeFinder

    def init(self, enemy):
        if not self.tryFindNearestHealthOrVest(enemy):
            enemy.aiData.healthPowerupDelay = Random.getInt(200, 500)

    def process(self, enemy, inputData):
        if enemy.aiData.route.hasPoints():
            self.movingLogic.followByRoute(enemy)
            inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if enemy.health >= enemy.aiData.criticalHealth:
            return EnemyState.patrolling

        if not enemy.aiData.route.hasPoints():
            return EnemyState.patrolling

        return None

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
