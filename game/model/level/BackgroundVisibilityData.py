from game.anx.CommonConstants import CommonConstants
from game.calc.Sphere import Sphere
from game.lib.Math import Math


class BackgroundVisibilityData:

    def __init__(self):
        self.sphere = Sphere(CommonConstants.maxLevelSize, 8, 16, (Math.piHalf, CommonConstants.xAxis))
        self.visibleSphereElements = []
