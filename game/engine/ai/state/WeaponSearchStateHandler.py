from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.ai.common.PowerupFinder import PowerupFinder
from game.lib.Random import Random
from game.model.ai.EnemyState import EnemyState


class WeaponSearchStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        powerupFinder: PowerupFinder,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.powerupFinder = powerupFinder

    def init(self, enemy):
        if not self.powerupFinder.tryFindNearestWeapon(enemy):
            enemy.aiData.weaponPowerupDelay.set(Random.getInt(200, 500))

    def process(self, enemy, inputData):
        if enemy.aiData.route.hasPoints():
            self.movingLogic.followByRoute(enemy)
            inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if not enemy.aiData.route.hasPoints():
            return EnemyState.patrolling

        return None
