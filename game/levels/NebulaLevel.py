from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.levels.builder.CeilingBuilder import CeilingHole
from game.levels.builder.Doorway import Doorway
from game.levels.builder.DoorwayBorder import DoorwayBorder
from game.levels.builder.LevelBuilder import LevelBuilder
from game.levels.builder.WallBorder import WallBorder
from game.levels.builder.WallInfo import WallInfo
from game.model.level.Level import Level
from game.model.level.LevelAreas import PowerupArea, RespawnArea
from game.model.level.LevelSegmentJoinLine import LevelSegmentJoinLine
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
        self.firstFloorHeight = 3
        self.secondFloorHeight = 6
        self.secondFloorSlabHeight = 0.3
        self.secondFloorZ = self.firstFloorHeight + self.secondFloorSlabHeight
        builder = LevelBuilder(self)
        self.makeFirstFloor(builder)
        self.makeSecondFloor(builder)
        self.makeLights(builder)
        self.makeJoinLines()
        self.makePowerupAreas()
        self.makeRespawnAreas()

    def makeFirstFloor(self, builder):
        builder.buildFlatFloor(Vector3(0, 0, 0), 45, 50, Material.rock1)
        builder.buildFlatFloor(Vector3(45, 0, 0), 55, 50, Material.rock1)
        builder.buildFlatFloor(Vector3(0, 50, 0), 45, 50, Material.rock1)
        builder.buildFlatFloor(Vector3(45, 50, 0), 55, 50, Material.rock1)

        builder.buildWalls(
            Vector3(0, 0, 0),
            WallInfo(
                Vector3(0, 30, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(15, 30, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(15, 40, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(0, 40, 0),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(0, 90, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(10, 100, 0),
                Vector3(1, -1, 0).getNormalized(),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(25, 100, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(25, 95, 0),
                Vector3(-1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(40, 95, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(40, 100, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(80, 100, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(80, 80, 0),
                Vector3(-1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(100, 80, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(100, 20, 0),
                Vector3(-1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(80, 0, 0),
                Vector3(-1, 1, 0).getNormalized(),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(65, 0, 0),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(65, 10, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(70, 10, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(70, 15, 0),
                Vector3(1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(45, 15, 0),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(45, 10, 0),
                Vector3(-1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(55, 10, 0),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(55, 0, 0),
                Vector3(-1, 0, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(45, 0, 0),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(0, 0, 0),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
        )

        builder.buildPillar(Vector3(40, 50, self.firstFloorZ), 1, self.firstFloorHeight, Material.construction3)
        builder.buildPillar(Vector3(65, 50, self.firstFloorZ), 1, self.firstFloorHeight, Material.construction3)

        centerStairZ = self.firstFloorZ + self.firstFloorHeight / 2
        # центральная лестница
        builder.buildStair(
            Vector3(90, 50, self.firstFloorZ),
            5,
            5,
            Vector3(90, 55, self.firstFloorZ),
            Vector3(95, 55, centerStairZ),
            10,
            5,
            Material.construction17,
        )

        builder.buildPillar(Vector3(90, 49.5, self.firstFloorZ), 0.5, 1.0, Material.construction3, withTop=True, excludeWalls=[Vector3(1, 0, 0)])
        builder.buildPillar(Vector3(90, 55, self.firstFloorZ), 0.5, 1.0, Material.construction3, withTop=True, excludeWalls=[Vector3(1, 0, 0)])
        builder.buildPillar(
            Vector3(94.5, 49.5, self.firstFloorZ),
            0.5,
            centerStairZ + 1.0,
            Material.construction3,
            withTop=True,
            excludeWalls=[Vector3(-1, 0, 0), Vector3(0, -1, 0)],
        )
        builder.buildPillar(
            Vector3(94.5, 55, self.firstFloorZ),
            0.5,
            centerStairZ + 1.0,
            Material.construction3,
            withTop=True,
            excludeWalls=[Vector3(-1, 0, 0), Vector3(0, 1, 0)],
        )
        builder.buildPillar(
            Vector3(94.5, 45, self.firstFloorZ),
            0.5,
            self.secondFloorZ + 1.0,
            Material.construction3,
            withTop=True,
            excludeWalls=[Vector3(0, 1, 0)],
        )
        builder.buildPillar(
            Vector3(94.5, 59.5, self.firstFloorZ),
            0.5,
            self.secondFloorZ + 1.0,
            Material.construction3,
            withTop=True,
            excludeWalls=[Vector3(0, -1, 0)],
        )

        builder.buildWalls(
            Vector3(95, 45, self.firstFloorZ),
            WallInfo(
                Vector3(100, 45, self.firstFloorZ),
                Vector3(0, -1, 0),
                self.firstFloorHeight,
                Material.construction3,
            ),
        )
        builder.buildWalls(
            Vector3(95, 60, self.firstFloorZ),
            WallInfo(
                Vector3(100, 60, self.firstFloorZ),
                Vector3(0, 1, 0),
                self.firstFloorHeight,
                Material.construction3,
            ),
        )

        builder.buildWall(
            Vector3(90.5, 49.5, self.firstFloorZ),
            Vector3(94.5, 49.5, self.firstFloorZ),
            Vector3(0, -1, 0),
            1.0,
            centerStairZ + 1.0,
            Material.construction3,
        )
        builder.buildWall(
            Vector3(90.5, 50, self.firstFloorZ),
            Vector3(94.5, 50, self.firstFloorZ),
            Vector3(0, 1, 0),
            1.0,
            centerStairZ + 1.0,
            Material.construction3,
        )
        builder.buildFloor(
            Vector3(90.5, 50, 1.0),
            Vector3(90.5, 49.5, 1.0),
            Vector3(94.5, 50, centerStairZ + 1.0),
            Vector3(94.5, 49.5, centerStairZ + 1.0),
            Material.construction3,
        )

        builder.buildWall(
            Vector3(90.5, 55, self.firstFloorZ),
            Vector3(94.5, 55, self.firstFloorZ),
            Vector3(0, -1, 0),
            1.0,
            centerStairZ + 1.0,
            Material.construction3,
        )
        builder.buildWall(
            Vector3(90.5, 55.5, self.firstFloorZ),
            Vector3(94.5, 55.5, self.firstFloorZ),
            Vector3(0, 1, 0),
            1.0,
            centerStairZ + 1.0,
            Material.construction3,
        )
        builder.buildFloor(
            Vector3(90.5, 55.5, 1.0),
            Vector3(90.5, 55, 1.0),
            Vector3(94.5, 55.5, centerStairZ + 1.0),
            Vector3(94.5, 55, centerStairZ + 1.0),
            Material.construction3,
        )

        builder.buildWall(
            Vector3(95, 49.5, self.firstFloorZ),
            Vector3(95, 45.5, self.firstFloorZ),
            Vector3(1, 0, 0),
            centerStairZ + 1.0,
            self.secondFloorZ + 1.0,
            Material.construction3,
        )
        builder.buildWall(
            Vector3(94.5, 49.5, self.firstFloorZ),
            Vector3(94.5, 45.5, self.firstFloorZ),
            Vector3(-1, 0, 0),
            centerStairZ + 1.0,
            self.secondFloorZ + 1.0,
            Material.construction3,
        )
        builder.buildFloor(
            Vector3(95, 49.5, centerStairZ + 1.0),
            Vector3(94.5, 49.5, centerStairZ + 1.0),
            Vector3(95, 45.5, self.secondFloorZ + 1.0),
            Vector3(94.5, 45.5, self.secondFloorZ + 1.0),
            Material.construction3,
        )

        builder.buildWall(
            Vector3(95, 55.5, self.firstFloorZ),
            Vector3(95, 59.5, self.firstFloorZ),
            Vector3(1, 0, 0),
            centerStairZ + 1.0,
            self.secondFloorZ + 1.0,
            Material.construction3,
        )
        builder.buildWall(
            Vector3(94.5, 55.5, self.firstFloorZ),
            Vector3(94.5, 59.5, self.firstFloorZ),
            Vector3(-1, 0, 0),
            centerStairZ + 1.0,
            self.secondFloorZ + 1.0,
            Material.construction3,
        )
        builder.buildFloor(
            Vector3(94.5, 55.5, centerStairZ + 1.0),
            Vector3(95, 55.5, centerStairZ + 1.0),
            Vector3(94.5, 59.5, self.secondFloorZ + 1.0),
            Vector3(95, 59.5, self.secondFloorZ + 1.0),
            Material.construction3,
        )

        builder.buildRectSlab(
            Vector3(95, 50, self.firstFloorZ + self.firstFloorHeight / 2), 5, 5, 0.1, Material.construction3, Material.edgeMetal2, 2.5
        )

        # левая лестница на второй этаж
        builder.buildStair(
            Vector3(95, 55, self.firstFloorZ + self.firstFloorHeight / 2),
            5,
            5,
            Vector3(95, 55, self.firstFloorZ + self.firstFloorHeight / 2),
            Vector3(95, 60, self.firstFloorZ + self.secondFloorSlabHeight + self.firstFloorHeight),
            10,
            5,
            Material.construction17,
        )

        # правая лестница на второй этаж
        builder.buildStair(
            Vector3(95, 45, self.firstFloorZ + self.firstFloorHeight / 2),
            5,
            5,
            Vector3(100, 50, self.firstFloorZ + self.firstFloorHeight / 2),
            Vector3(100, 45, self.firstFloorZ + self.secondFloorSlabHeight + self.firstFloorHeight),
            10,
            5,
            Material.construction17,
        )

    def makeSecondFloor(self, builder):
        builder.buildRectSlab(Vector3(0, 0, self.secondFloorZ), 100, 15, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(0, 15, self.secondFloorZ), 10, 10, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(0, 25, self.secondFloorZ), 20, 75, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(20, 90, self.secondFloorZ), 10, 10, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(30, 80, self.secondFloorZ), 70, 20, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(90, 60, self.secondFloorZ), 10, 20, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(90, 25, self.secondFloorZ), 10, 20, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(80, 15, self.secondFloorZ), 20, 10, self.secondFloorSlabHeight, Material.construction3, Material.edgeMetal2)

        builder.buildRectSlab(Vector3(35, 15, self.secondFloorZ), 8, 32, self.secondFloorSlabHeight, Material.construction11, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(35, 47, self.secondFloorZ), 34, 8, self.secondFloorSlabHeight, Material.construction11, Material.edgeMetal2)
        builder.buildRectSlab(Vector3(61, 55, self.secondFloorZ), 8, 25, self.secondFloorSlabHeight, Material.construction11, Material.edgeMetal2)

        builder.buildWall(
            Vector3(100, 60, self.firstFloorZ + self.firstFloorHeight),
            Vector3(100, 40, self.firstFloorZ + self.firstFloorHeight),
            Vector3(-1, 0, 0),
            self.secondFloorSlabHeight,
            self.secondFloorSlabHeight,
            Material.construction7,
        )

        builder.buildWalls(
            Vector3(0, 0, self.secondFloorZ),
            WallInfo(
                Vector3(0, 100, self.secondFloorZ),
                Vector3(1, 0, 0),
                self.secondFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(100, 100, self.secondFloorZ),
                Vector3(0, -1, 0),
                self.secondFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(100, 0, self.secondFloorZ),
                Vector3(-1, 0, 0),
                self.secondFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
            WallInfo(
                Vector3(0, 0, self.secondFloorZ),
                Vector3(0, 1, 0),
                self.secondFloorHeight,
                Material.construction7,
                visualSize=4.0,
            ),
        )

        builder.buildCeiling(Vector3(0, 0, self.secondFloorZ + self.secondFloorHeight), 100, 100, Material.construction7, CeilingHole(80, 80))

    def makeLights(self, builder):
        builder.buildLight(Vector3(50, 50, self.secondFloorZ + self.secondFloorHeight + 10), 2.0)

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(45, 10, self.firstFloorZ + 1), Vector3(45, 90, self.firstFloorZ + 1)))

        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 15, self.secondFloorZ), Vector3(100, 15, self.secondFloorZ), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(10, 15, self.secondFloorZ), Vector3(10, 100, self.secondFloorZ), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(20, 80, self.secondFloorZ), Vector3(90, 80, self.secondFloorZ), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(90, 15, self.secondFloorZ), Vector3(90, 80, self.secondFloorZ), CommonConstants.zAxis))

        z = self.secondFloorZ + self.secondFloorHeight
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 0, z), Vector3(100, 0, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 0, z), Vector3(0, 100, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 0, z), Vector3(100, 100, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(0, 100, z), Vector3(100, 100, z), CommonConstants.zAxis))

        self.addJoinLine(LevelSegmentJoinLine(Vector3(20, 20, z), Vector3(80, 20, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(20, 20, z), Vector3(20, 80, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(80, 20, z), Vector3(80, 80, z), CommonConstants.zAxis))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(20, 80, z), Vector3(80, 80, z), CommonConstants.zAxis))

    def makePowerupAreas(self):
        self.addPowerupArea(PowerupArea(Vector3(50, 50, self.firstFloorZ), Vector3(50, 50, self.firstFloorZ), 40))

        self.addPowerupArea(PowerupArea(Vector3(10, 7, self.secondFloorZ), Vector3(90, 7, self.secondFloorZ), 7))
        self.addPowerupArea(PowerupArea(Vector3(5, 20, self.secondFloorZ), Vector3(5, 20, self.secondFloorZ), 5))
        self.addPowerupArea(PowerupArea(Vector3(10, 35, self.secondFloorZ), Vector3(10, 90, self.secondFloorZ), 10))
        self.addPowerupArea(PowerupArea(Vector3(25, 95, self.secondFloorZ), Vector3(25, 95, self.secondFloorZ), 5))
        self.addPowerupArea(PowerupArea(Vector3(40, 90, self.secondFloorZ), Vector3(90, 90, self.secondFloorZ), 10))
        self.addPowerupArea(PowerupArea(Vector3(95, 75, self.secondFloorZ), Vector3(95, 65, self.secondFloorZ), 5))
        self.addPowerupArea(PowerupArea(Vector3(95, 40, self.secondFloorZ), Vector3(95, 30, self.secondFloorZ), 5))
        self.addPowerupArea(PowerupArea(Vector3(85, 20, self.secondFloorZ), Vector3(95, 20, self.secondFloorZ), 5))

    def makeRespawnAreas(self):
        self.addRespawnArea(RespawnArea(Vector3(5, 5, self.secondFloorZ), Vector3(95, 5, self.secondFloorZ), 5, Vector3(0, 1, 0)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        # first floor
        yield SplitPlane(Vector3(90, 50, self.firstFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(92, 50, self.firstFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(92, 55, self.firstFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(95, 52, self.firstFloorZ), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(96, 52, self.firstFloorZ + 1.0), Vector3(0, 0, 1))
        yield SplitPlane(Vector3(96, 60, self.firstFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(96, 45, self.firstFloorZ), Vector3(0, -1, 0))

        # second floor
        yield SplitPlane(Vector3(20, 50, self.secondFloorZ), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(15, 25, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(15, 15, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(10, 20, self.secondFloorZ), Vector3(1, 0, 0))

        yield SplitPlane(Vector3(80, 50, self.secondFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(90, 50, self.secondFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(95, 80, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(85, 80, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(95, 60, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(95, 45, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(95, 25, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(85, 25, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(80, 20, self.secondFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(95, 15, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(85, 15, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(85, 25, self.secondFloorZ), Vector3(0, 1, 0))

        yield SplitPlane(Vector3(50, 15, self.secondFloorZ), Vector3(0, 1, 0))

        yield SplitPlane(Vector3(50, 80, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(30, 90, self.secondFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(25, 90, self.secondFloorZ), Vector3(0, -1, 0))

        # bridge
        yield SplitPlane(Vector3(35, 50, self.secondFloorZ), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(69, 50, self.secondFloorZ), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(50, 55, self.secondFloorZ), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(50, 47, self.secondFloorZ), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(43, 30, self.secondFloorZ), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(61, 70, self.secondFloorZ), Vector3(-1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(50, 50, self.secondFloorZ), Vector3(0, 0, 1))
        yield SplitPlane(Vector3(50, 50, self.secondFloorZ + self.secondFloorHeight), Vector3(0, 0, 1))
        yield SplitPlane(Vector3(45, 50, self.firstFloorZ + 1), Vector3(1, 0, 0))

    def getPlayerInitInfo(self):
        return (Vector3(80, 53, self.firstFloorZ), Vector3(-1, 0, 0).getNormalized(), Pistol)

    def getEnemyInitInfo(self):
        return [
            (Vector3(50, 50, self.firstFloorZ), Vector3(0, -1, 0).getNormalized(), Pistol),
            # (Vector3(50, 55, self.firstFloorZ), Vector3(0, -1, 0).getNormalized(), Pistol),
        ]
