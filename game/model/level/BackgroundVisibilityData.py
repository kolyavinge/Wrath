from game.anx.CommonConstants import CommonConstants
from game.calc.BSPTree import BSPTree, SplitPlane
from game.calc.Sphere import Sphere
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class BackgroundVisibilityData:

    def __init__(self):
        self.sphere = Sphere(CommonConstants.maxLevelSize, 8, 16, (Math.piHalf, CommonConstants.xAxis))

        self.sphereBSPTree = BSPTree(
            self.sphere.getAllSpherePoints(),
            lambda point: point.vertex,
            [
                # отсекаем верх и низ сферы
                SplitPlane(Vector3(0, 0, 0), Vector3(0, 0, 1)),
                # если смотреть сверху: отсекаем с севера на юг
                SplitPlane(Vector3(0, 0, 1), Vector3(1, 0, 0)),
                SplitPlane(Vector3(0, 0, -1), Vector3(1, 0, 0)),
                # и с запада на восток
                SplitPlane(Vector3(-1, 0, 1), Vector3(0, 1, 0)),
                SplitPlane(Vector3(1, 0, 1), Vector3(0, 1, 0)),
                SplitPlane(Vector3(-1, 0, -1), Vector3(0, 1, 0)),
                SplitPlane(Vector3(1, 0, -1), Vector3(0, 1, 0)),
            ],
        )

        self.visibleSphereElements = set()
