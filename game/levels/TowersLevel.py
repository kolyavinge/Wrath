from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.levels.builder.CeilingBuilder import CeilingHole
from game.levels.builder.Doorway import Doorway
from game.levels.builder.DoorwayBorder import DoorwayBorder
from game.levels.builder.LevelBuilder import LevelBuilder
from game.levels.builder.WallBorder import WallBorder
from game.levels.builder.WallInfo import WallInfo
from game.lib.Math import Math
from game.model.level.Ceiling import Ceiling
from game.model.level.Level import Level
from game.model.level.LevelSegmentJoinLine import LevelSegmentJoinLine
from game.model.level.PowerupArea import PowerupArea
from game.model.Material import Material


class TowersLevel(Level):

    def __init__(self):
        super().__init__()
        self.builder = LevelBuilder(self)
        self.makeMainFloor()
        self.makeMainLight()
        self.makeTower()
        self.setPlayerPosition()

    def makeMainFloor(self):
        material = Material.rock1
        self.builder.buildFlatFloor(Vector3(0, 0, 0), 100, 100, material, 3)
        self.builder.buildFlatFloor(Vector3(100, 0, 0), 100, 100, material, 3)
        self.builder.buildFlatFloor(Vector3(0, 100, 0), 100, 100, material, 3)
        self.builder.buildFlatFloor(Vector3(100, 100, 0), 100, 100, material, 3)

    def makeMainLight(self):
        self.builder.buildLight(Vector3(1, 1, 1), 2, "main")

    def makeTower(self):
        material = Material.ceilingMetal1
        edgeMaterial = Material.edgeMetal3
        self.builder.buildSlab(Vector3(10, 10, 4), Vector3(30, 10, 4), Vector3(10, 30, 4), Vector3(30, 30, 4), 0.5, material, edgeMaterial)
        self.builder.buildSlab(Vector3(12, 12, 7), Vector3(28, 12, 7), Vector3(12, 28, 7), Vector3(28, 28, 7), 0.5, material, edgeMaterial)
        self.builder.buildSlab(Vector3(14, 14, 10), Vector3(26, 14, 10), Vector3(14, 26, 10), Vector3(26, 26, 10), 0.5, material, edgeMaterial)
        self.builder.buildSlab(Vector3(16, 16, 13), Vector3(24, 16, 13), Vector3(16, 24, 13), Vector3(24, 24, 13), 0.5, material, edgeMaterial)

        material = Material.ceilingMetal1
        self.builder.buildPillar(Vector3(11, 11, 0), 1, 3.5, material)
        self.builder.buildPillar(Vector3(28, 11, 0), 1, 3.5, material)
        self.builder.buildPillar(Vector3(11, 28, 0), 1, 3.5, material)
        self.builder.buildPillar(Vector3(28, 28, 0), 1, 3.5, material)

        self.builder.buildPillar(Vector3(13, 13, 4), 1, 2.5, material)
        self.builder.buildPillar(Vector3(26, 13, 4), 1, 2.5, material)
        self.builder.buildPillar(Vector3(13, 26, 4), 1, 2.5, material)
        self.builder.buildPillar(Vector3(26, 26, 4), 1, 2.5, material)

        self.builder.buildPillar(Vector3(15, 15, 7), 1, 2.5, material)
        self.builder.buildPillar(Vector3(24, 15, 7), 1, 2.5, material)
        self.builder.buildPillar(Vector3(15, 24, 7), 1, 2.5, material)
        self.builder.buildPillar(Vector3(24, 24, 7), 1, 2.5, material)

        self.builder.buildPillar(Vector3(17, 17, 10), 1, 2.5, material)
        self.builder.buildPillar(Vector3(22, 17, 10), 1, 2.5, material)
        self.builder.buildPillar(Vector3(17, 22, 10), 1, 2.5, material)
        self.builder.buildPillar(Vector3(22, 22, 10), 1, 2.5, material)

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 0, 0), Vector3(100, 100, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 100, 0), Vector3(100, 200, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 100, 0), Vector3(100, 100, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 100, 0), Vector3(200, 100, 0)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        yield SplitPlane(Vector3(50, 50, 2), Vector3(0, 0, 1))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(0, 0, 0), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(200, 0, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(100, 0, 0), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(100, 200, 0), Vector3(0, 1, 0))

        yield SplitPlane(Vector3(100, 100, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(50, 100, 0), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(150, 100, 0), Vector3(0, 1, 0))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(1, 1, 0)
        self.playerFrontNormal = Vector3(1, 1, 0).getNormalized()
