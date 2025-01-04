from game.anx.CommonConstants import CommonConstants
from game.model.level.Construction import Construction


class Ceiling(Construction):

    def __init__(self):
        super().__init__()
        self.frontNormal = CommonConstants.down
        self.visualSize = 2
