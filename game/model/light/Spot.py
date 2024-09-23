from game.anx.CommonConstants import CommonConstants
from game.model.light.Lamp import Lamp


class Spot(Lamp):

    def __init__(self):
        super().__init__()
        self.direction = CommonConstants.down
        self.attenuation = 1.0
        self.cutoffCos = 0.0
