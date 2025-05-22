from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.model.ai.EnemyState import EnemyState
from game.model.ai.Route import Route


class HealthSearchStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def init(self, enemy):
        pass

    def process(self, enemy, inputData):
        if enemy.aiData.route.hasPoints():
            self.movingLogic.followByRoute(enemy)
            inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        return None
