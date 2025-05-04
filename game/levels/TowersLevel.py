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
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle


class TowersLevel(Level):

    def __init__(self):
        super().__init__()
        builder = LevelBuilder(self)
        self.minZ = 2
        self.makeArea1(builder)
        self.makeArea2(builder)
        self.makeArea3(builder)
        self.makeJoinLines()

    def makeArea1(self, builder):
        # floor
        builder.buildRectSlab(Vector3(10, 10, self.minZ), 80, 80, 1, Material.rock1, Material.rock1)

        # tower
        x = 40
        y = 40
        material = Material.ceilingMetal1
        edgeMaterial = Material.edgeMetal3
        builder.buildRectSlab(Vector3(x, y, self.minZ + 4), 20, 20, 0.5, material, edgeMaterial)
        builder.buildRectSlab(Vector3(x + 2, y + 2, self.minZ + 7), 16, 16, 0.5, material, edgeMaterial)
        builder.buildRectSlab(Vector3(x + 4, y + 4, self.minZ + 10), 12, 12, 0.5, material, edgeMaterial)
        builder.buildRectSlab(Vector3(x + 6, y + 6, self.minZ + 13), 8, 8, 0.5, material, edgeMaterial)

        material = Material.ceilingMetal1
        builder.buildPillar(Vector3(x + 1, y + 1, self.minZ), 1, 3.5, material)
        builder.buildPillar(Vector3(x + 18, y + 1, self.minZ), 1, 3.5, material)
        builder.buildPillar(Vector3(x + 1, y + 18, self.minZ), 1, 3.5, material)
        builder.buildPillar(Vector3(x + 18, y + 18, self.minZ), 1, 3.5, material)

        builder.buildPillar(Vector3(x + 3, y + 3, self.minZ + 4), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 16, y + 3, self.minZ + 4), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 3, y + 16, self.minZ + 4), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 16, y + 16, self.minZ + 4), 1, 2.5, material)

        builder.buildPillar(Vector3(x + 5, y + 5, self.minZ + 7), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 14, y + 5, self.minZ + 7), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 5, y + 14, self.minZ + 7), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 14, y + 14, self.minZ + 7), 1, 2.5, material)

        builder.buildPillar(Vector3(x + 7, y + 7, self.minZ + 10), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 12, y + 7, self.minZ + 10), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 7, y + 12, self.minZ + 10), 1, 2.5, material)
        builder.buildPillar(Vector3(x + 12, y + 12, self.minZ + 10), 1, 2.5, material)

        # light
        builder.buildLight(Vector3(1, 1, self.minZ + 2), 2)

        self.addPowerupArea(PowerupArea(Vector3(50, 50, self.minZ), Vector3(50, 50, self.minZ), 40))

    def makeArea2(self, builder):
        # floor
        builder.buildRectSlab(Vector3(20, 150, self.minZ + 2), 80, 80, 1, Material.rock1, Material.rock1)

        # light
        builder.buildLight(Vector3(20, 150, self.minZ + 4), 2)

        self.addPowerupArea(PowerupArea(Vector3(60, 190, self.minZ + 2), Vector3(60, 190, self.minZ + 2), 40))

    def makeArea3(self, builder):
        # floor
        builder.buildRectSlab(Vector3(150, 50, self.minZ + 5), 80, 80, 1, Material.rock1, Material.rock1)

        # light
        builder.buildLight(Vector3(150, 50, self.minZ + 7), 2)

        self.addPowerupArea(PowerupArea(Vector3(190, 90, self.minZ + 5), Vector3(190, 90, self.minZ + 5), 40))

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(120, 0, self.minZ + 2), Vector3(120, 100, self.minZ + 2)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 100, self.minZ + 2), Vector3(90, 100, self.minZ + 2)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        # area1
        yield SplitPlane(Vector3(0, 0, self.minZ + 3.5), Vector3(0, 0, 1))
        yield SplitPlane(Vector3(45, 10, self.minZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(45, 90, self.minZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(10, 45, self.minZ), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(90, 45, self.minZ), Vector3(-1, 0, 0))

        # area2
        yield SplitPlane(Vector3(50, 150, self.minZ + 2), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(50, 230, self.minZ + 2), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(20, 200, self.minZ + 2), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(100, 200, self.minZ + 2), Vector3(-1, 0, 0))

        # area3
        yield SplitPlane(Vector3(200, 50, self.minZ + 5), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(200, 130, self.minZ + 5), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(150, 100, self.minZ + 5), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(230, 100, self.minZ + 5), Vector3(-1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(120, 0, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(0, 100, 0), Vector3(0, 1, 0))

    def getPlayerInitInfo(self):
        return (Vector3(30, 30, self.minZ), Vector3(-1, -1, 0).getNormalized(), Pistol)

    def getEnemyInitInfo(self):
        return [
            (Vector3(10, 10, self.minZ), Vector3(1, 1, 0).getNormalized(), Plasma),
            # (Vector3(25, 25, self.minZ), Vector3(1, 0, 0).getNormalized(), Launcher),
        ]
