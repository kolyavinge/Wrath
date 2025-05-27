from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.ai.common.PowerupFinder import PowerupFinder
from game.engine.GameData import GameData
from game.lib.Random import Random
from game.model.ai.EnemyState import EnemyState


class HealthSearchStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        powerupFinder: PowerupFinder,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.powerupFinder = powerupFinder

    def init(self, enemy):
        if not self.powerupFinder.tryFindNearestHealthOrVest(enemy):
            enemy.aiData.healthPowerupDelay.set(Random.getInt(200, 500))

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
