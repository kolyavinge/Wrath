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
from game.model.weapon.Sniper import Sniper


class NebulaLevel(Level):

    def __init__(self):
        super().__init__()
        self.firstFloorZ = 0
        self.secondFloorZ = 4.5
        builder = LevelBuilder(self)
        self.makeFirstFloor(builder)
        self.makeSecondFloor(builder)
        self.makeJoinLines()

    def makeFirstFloor(self, builder):
        floorHeight = 4

        builder.buildFlatFloor(Vector3(0, 0, 0), 100, 100, Material.rock1)

        builder.buildWalls(
            Vector3(0, 0, 0),
            WallInfo(
                Vector3(0, 30, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(15, 30, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(15, 40, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(0, 40, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(0, 90, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(10, 100, 0),
                Vector3(1, -1, 0).getNormalized(),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(25, 100, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(25, 95, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(40, 95, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(40, 100, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(80, 100, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(80, 80, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(100, 80, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(100, 20, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(80, 0, 0),
                Vector3(-1, 1, 0).getNormalized(),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(65, 0, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(65, 10, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(70, 10, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(70, 15, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(45, 15, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(45, 10, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(55, 10, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(55, 0, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(0, 0, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.construction7,
            ),
        )

        builder.buildPillar(Vector3(40, 50, self.firstFloorZ), 1, floorHeight, Material.construction3)
        builder.buildPillar(Vector3(65, 50, self.firstFloorZ), 1, floorHeight, Material.construction3)

        builder.buildStair(
            Vector3(90, 50, self.firstFloorZ),
            5,
            5,
            Vector3(90, 55, self.firstFloorZ),
            Vector3(95, 55, self.firstFloorZ + floorHeight / 2),
            10,
            5,
            Material.construction17,
        )
        builder.buildRectSlab(Vector3(95, 50, self.firstFloorZ + floorHeight / 2), 5, 5, 0.1, Material.construction3, Material.edgeMetal2)
        # левая лестница на второй этаж
        builder.buildStair(
            Vector3(95, 55, self.firstFloorZ + floorHeight / 2),
            5,
            5,
            Vector3(95, 55, self.firstFloorZ + floorHeight / 2),
            Vector3(95, 60, self.firstFloorZ + 0.5 + floorHeight),
            10,
            5,
            Material.construction17,
        )
        # правая лестница на второй этаж
        builder.buildStair(
            Vector3(95, 50, self.firstFloorZ + floorHeight / 2),
            5,
            5,
            Vector3(100, 50, self.firstFloorZ + floorHeight / 2),
            Vector3(100, 45, self.firstFloorZ + 0.5 + floorHeight),
            10,
            5,
            Material.construction17,
        )

        builder.buildLight(Vector3(50, 50, self.secondFloorZ - 0.1), 1.0, "global")
        self.addPowerupArea(PowerupArea(Vector3(22, 14, self.firstFloorZ), Vector3(22, 14, self.firstFloorZ), 1))

    def makeSecondFloor(self, builder):
        floorHeight = 8

        slabHeight = 0.5
        builder.buildRectSlab(Vector3(0, 0, self.secondFloorZ), 100, 15, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(0, 15, self.secondFloorZ), 10, 10, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(0, 25, self.secondFloorZ), 15, 75, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(15, 90, self.secondFloorZ), 15, 15, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(15, 90, self.secondFloorZ), 15, 15, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(30, 80, self.secondFloorZ), 70, 20, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(90, 60, self.secondFloorZ), 10, 20, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(90, 25, self.secondFloorZ), 10, 20, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(80, 15, self.secondFloorZ), 20, 10, slabHeight, Material.construction3, Material.edgeMetal2)

        builder.buildRectSlab(Vector3(35, 15, self.secondFloorZ), 10, 30, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(35, 45, self.secondFloorZ), 35, 10, slabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(60, 55, self.secondFloorZ), 10, 25, slabHeight, Material.construction3, Material.edgeMetal2)

        builder.buildWalls(
            Vector3(0, 0, self.secondFloorZ),
            WallInfo(
                Vector3(0, 100, self.secondFloorZ),
                Vector3(1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(100, 100, self.secondFloorZ),
                Vector3(0, -1, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(100, 0, self.secondFloorZ),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.construction7,
            ),
            WallInfo(
                Vector3(0, 0, self.secondFloorZ),
                Vector3(0, 1, 0),
                floorHeight,
                Material.construction7,
            ),
        )

        builder.buildCeiling(Vector3(0, 0, self.secondFloorZ + floorHeight), 100, 100, Material.construction7, CeilingHole(80, 80))

        builder.buildLight(Vector3(50, 50, self.secondFloorZ + floorHeight), 1.0, "global")

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 50, self.secondFloorZ), Vector3(50, 50, self.secondFloorZ)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        yield SplitPlane(Vector3(90, 50, self.firstFloorZ + 1), Vector3(-1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(50, 50, self.firstFloorZ), Vector3(0, 0, 1))
        yield SplitPlane(Vector3(50, 50, self.secondFloorZ), Vector3(0, 0, 1))

    def getPlayerInitInfo(self):
        return (Vector3(20, 50, self.firstFloorZ), Vector3(1, 0, 0).getNormalized(), Pistol)

    def getEnemyInitInfo(self):
        return [
            (Vector3(50, 50, self.firstFloorZ), Vector3(1, 0, 0).getNormalized(), Pistol),
            (Vector3(88, 53, self.firstFloorZ), Vector3(-1, 0, 0).getNormalized(), Pistol),
        ]
