from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.model.ai.EnemyState import EnemyState


class WeaponSearchStateHandler:

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
        pass

    def getNewStateOrNone(self, enemy):
        return None
