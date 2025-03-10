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


class AuroraLevel(Level):

    def __init__(self):
        super().__init__()
        self.builder = LevelBuilder(self)
        self.makeMainRoom()
        self.makeLeftRoom()
        self.makeBottomRoom()
        self.makeLeftRoomPass()
        self.makeBottomRoomPass()
        self.makeLeftBottomRoomPass()
        self.makeRightPass()
        self.makeJoinLines()

    def makeMainRoom(self):
        # first floor
        firstFloorHeight = 4
        self.builder.buildWalls(
            Vector3(16, 11, 0),
            WallInfo(
                Vector3(16, 17, 0),
                Vector3(1, 0, 0),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
                None,
                Doorway(Vector3(16, 13, 0), 2, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.edgeMetal1)),
            ),
            WallInfo(
                Vector3(19, 20, 0),
                Vector3(1, -1, 0).getNormalized(),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
            WallInfo(
                Vector3(25, 20, 0),
                Vector3(0, -1, 0),
                firstFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
            WallInfo(
                Vector3(28, 17, 0),
                Vector3(-1, -1, 0).getNormalized(),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
            WallInfo(
                Vector3(28, 11, 0),
                Vector3(-1, 0, 0),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
            WallInfo(
                Vector3(25, 8, 0),
                Vector3(-1, 1, 0).getNormalized(),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
            WallInfo(
                Vector3(19, 8, 0),
                Vector3(0, 1, 0),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
                None,
                Doorway(Vector3(23, 8, 0), 2, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.edgeMetal1)),
            ),
            WallInfo(
                Vector3(16, 11, 0),
                Vector3(1, 1, 0).getNormalized(),
                firstFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.edgeMetal1, Material.edgeMetal1),
            ),
        )
        # balcony
        balconyHeight = 0.2
        balconyZ = firstFloorHeight + balconyHeight
        self.builder.buildSlab(
            Vector3(16, 17, balconyZ),
            Vector3(16, 11, balconyZ),
            Vector3(18, 17, balconyZ),
            Vector3(18, 11, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(28, 11, balconyZ),
            Vector3(28, 17, balconyZ),
            Vector3(26, 11, balconyZ),
            Vector3(26, 17, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(25, 20, balconyZ),
            Vector3(19, 20, balconyZ),
            Vector3(25, 18, balconyZ),
            Vector3(19, 18, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(19, 8, balconyZ),
            Vector3(25, 8, balconyZ),
            Vector3(19, 10, balconyZ),
            Vector3(25, 10, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(16, 11, balconyZ),
            Vector3(19, 8, balconyZ),
            Vector3(18, 11, balconyZ),
            Vector3(19, 10, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(19, 20, balconyZ),
            Vector3(16, 17, balconyZ),
            Vector3(19, 18, balconyZ),
            Vector3(18, 17, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(28, 17, balconyZ),
            Vector3(25, 20, balconyZ),
            Vector3(26, 17, balconyZ),
            Vector3(25, 18, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildSlab(
            Vector3(25, 8, balconyZ),
            Vector3(28, 11, balconyZ),
            Vector3(25, 10, balconyZ),
            Vector3(26, 11, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        # second floor
        secondFloorHeight = 3
        self.builder.buildWalls(
            Vector3(16, 11, balconyZ),
            WallInfo(
                Vector3(16, 17, balconyZ),
                Vector3(1, 0, 0),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 20, balconyZ),
                Vector3(1, -1, 0).getNormalized(),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 20, balconyZ),
                Vector3(0, -1, 0),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 17, balconyZ),
                Vector3(-1, -1, 0).getNormalized(),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 11, balconyZ),
                Vector3(-1, 0, 0),
                secondFloorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(28, 15, balconyZ), 2, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(25, 8, balconyZ),
                Vector3(-1, 1, 0).getNormalized(),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 8, balconyZ),
                Vector3(0, 1, 0),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(16, 11, balconyZ),
                Vector3(1, 1, 0).getNormalized(),
                secondFloorHeight,
                Material.wallMetal4,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        self.builder.buildPillar(Vector3(22 - 0.25, 18, 0), 0.5, firstFloorHeight, Material.ceilingMetal1)
        self.builder.buildFlatFloor(Vector3(16, 8, 0), 12, 12, Material.floorMetal1)
        ceilingZ = balconyZ + secondFloorHeight
        self.builder.buildCeiling(Vector3(16, 8, ceilingZ), 12, 12, Material.floorMetal3, CeilingHole(4, 4))
        self.builder.buildLight(Vector3(22, 14, 4), 0.5, "mainRoom")
        self.builder.buildLight(Vector3(22, 14, ceilingZ), 0.8, "mainRoom")
        self.addPowerupArea(PowerupArea(Vector3(22, 14, 0), Vector3(22, 14, 0), 6))

    def makeLeftRoom(self):
        floorHeight = 3
        self.builder.buildWalls(
            Vector3(9, 11, 0),
            WallInfo(
                Vector3(9, 17, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(10, 18, 0),
                Vector3(1, -1, 0).getNormalized(),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(13, 18, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(14, 17, 0),
                Vector3(-1, -1, 0).getNormalized(),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(14, 11, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(14, 15, 0), 2, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(13, 10, 0),
                Vector3(-1, 1, 0).getNormalized(),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(10, 10, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(12, 10, 0), 1, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(9, 11, 0),
                Vector3(1, 1, 0).getNormalized(),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        self.builder.buildFlatFloor(Vector3(9, 10, 0), 5, 8, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(9, 10, 3), 5, 8, Material.ceilingMetal1)
        self.builder.buildRectLamp(Vector3(11.5, 14, 3), Vector3(0, 0, -1), 0.05, 0.1, 1.0, Vector3(1, 0, 0), Material.ceilingMetal2),

    def makeBottomRoom(self):
        floorHeight = 3
        self.builder.buildWalls(
            Vector3(16, 1, 0),
            WallInfo(
                Vector3(16, 6, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(16, 3, 0), 1, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(28, 6, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(21, 6, 0), 2, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(28, 1, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(28, 4, 0), 1, 2.2, Material.floorMetal3, DoorwayBorder(0.3, 0.2, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(16, 1, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.wallMetal5,
                WallBorder(0.4, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        self.builder.buildFlatFloor(Vector3(16, 1, 0), 12, 5, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(16, 1, 3), 12, 5, Material.ceilingMetal1)
        self.builder.buildRectLamp(Vector3(22, 3.5, 3), Vector3(0, 0, -1), 0.05, 0.1, 1.0, Vector3(1, 0, 0), Material.ceilingMetal2),

    def makeLeftRoomPass(self):
        self.builder.wallBuilder.makeSolidWall(Vector3(14, 15, 0), Vector3(16, 15, 0), Vector3(0, -1, 0), 2.2, Material.ceilingMetal2)
        self.builder.wallBuilder.makeSolidWall(Vector3(14, 13, 0), Vector3(16, 13, 0), Vector3(0, 1, 0), 2.2, Material.ceilingMetal2)
        self.builder.buildFlatFloor(Vector3(14, 13, 0), 2, 2, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(14, 13, 2.2), 2, 2, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(15, 14, 2.2), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

    def makeBottomRoomPass(self):
        self.builder.wallBuilder.makeSolidWall(Vector3(21, 8, 0), Vector3(21, 6, 0), Vector3(1, 0, 0), 2.2, Material.ceilingMetal2)
        self.builder.wallBuilder.makeSolidWall(Vector3(23, 8, 0), Vector3(23, 6, 0), Vector3(-1, 0, 0), 2.2, Material.ceilingMetal2)
        self.builder.buildFlatFloor(Vector3(21, 6, 0), 2, 2, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(21, 6, 2.2), 2, 2, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(22, 7, 2.2), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

    def makeLeftBottomRoomPass(self):
        floorHeight = 3
        self.builder.buildWalls(
            Vector3(11, 10, 0),
            WallInfo(
                Vector3(10.5, 10, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(10.5, 6, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(14, 2.5, 0),
                Vector3(1, 1, 0).getNormalized(),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(16, 2.5, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(16, 3, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.floorMetal4,
            ),
        )
        self.builder.buildWalls(
            Vector3(12, 10, 0),
            WallInfo(
                Vector3(12.5, 10, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(12.5, 6, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(14, 4.5, 0),
                Vector3(-1, -1, 0).getNormalized(),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(16, 4.5, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.floorMetal4,
            ),
            WallInfo(
                Vector3(16, 4, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.floorMetal4,
            ),
        )

        self.builder.buildFlatFloor(Vector3(10, 6, 0), 3, 4, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(10, 6, 2.2), 3, 4, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(11.5, 8, 2.2), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

        self.builder.buildFlatFloor(Vector3(10, 2, 0), 4, 4, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(10, 2, 2.2), 4, 4, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(12.5, 5, 2.2), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

        self.builder.buildFlatFloor(Vector3(14, 2, 0), 2, 3, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(14, 2, 2.2), 2, 3, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(15, 3.5, 2.2), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

    def makeRightPass(self):
        floorHeight = 3
        self.builder.buildWalls(
            Vector3(28, 3, 0),
            WallInfo(
                Vector3(28, 2.5, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal5,
            ),
            WallInfo(
                Vector3(32, 2.5, 0),
                Vector3(0, 1, 0),
                floorHeight,
                Material.wallMetal5,
            ),
            WallInfo(
                Vector3(32, 4.5, 0),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.wallMetal5,
            ),
            WallInfo(
                Vector3(32, 6.5, 2),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.wallMetal3,
            ),
            WallInfo(
                Vector3(32, 15, 2),
                Vector3(-1, 0, 0),
                floorHeight,
                Material.wallMetal3,
            ),
            WallInfo(
                Vector3(30, 15, 2),
                Vector3(0, -1, 0),
                floorHeight,
                Material.wallMetal3,
            ),
            WallInfo(
                Vector3(28, 15, 4.2),
                Vector3(0, -1, 0),
                floorHeight,
                Material.wallMetal3,
            ),
        )
        self.builder.buildWalls(
            Vector3(28, 4, 0),
            WallInfo(
                Vector3(28, 4.5, 0),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal5,
            ),
            WallInfo(
                Vector3(30, 4.5, 0),
                Vector3(0, -1, 0),
                floorHeight,
                Material.wallMetal5,
            ),
            WallInfo(
                Vector3(30, 6.5, 2),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal3,
            ),
            WallInfo(
                Vector3(30, 13, 2),
                Vector3(1, 0, 0),
                floorHeight,
                Material.wallMetal3,
            ),
            WallInfo(
                Vector3(28, 13, 4.2),
                Vector3(0, 1, 0),
                floorHeight,
                Material.wallMetal3,
            ),
        )
        self.builder.buildFlatFloor(Vector3(28, 2.5, 0), 4, 2, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(28, 2.5, 3), 4, 2, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(30, 3.5, 3), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

        self.builder.buildStair(Vector3(30, 4.5, 0), 2, 2, Vector3(30, 4.5, 0), Vector3(30, 6.5, 2), 9, 2, Material.wallMetal9)
        ceiling = Ceiling()
        ceiling.downLeft = Vector3(30, 4.5, 3)
        ceiling.downRight = Vector3(32, 4.5, 3)
        ceiling.upLeft = Vector3(30, 6.5, 5)
        ceiling.upRight = Vector3(32, 6.5, 5)
        ceiling.frontNormal = Geometry.rotatePoint(
            ceiling.downLeft.getDirectionTo(ceiling.upLeft).getNormalized(), Vector3(1, 0, 0), CommonConstants.axisOrigin, -Math.piHalf
        )
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)
        self.builder.buildRoundLamp(Vector3(31, 5.5, 4), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

        self.builder.buildFlatFloor(Vector3(30, 6.5, 2), 2, 8.5, Material.floorMetal1)
        self.builder.buildCeiling(Vector3(30, 6.5, 5), 2, 9, Material.ceilingMetal1)
        self.builder.buildRoundLamp(Vector3(31, 10, 5), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

        self.builder.buildStair(Vector3(28, 13, 2), 2, 2, Vector3(30, 13, 2), Vector3(28, 13, 4.2), 9, 2, Material.wallMetal9)
        ceiling = Ceiling()
        ceiling.downLeft = Vector3(30, 13, 5)
        ceiling.downRight = Vector3(30, 15, 5)
        ceiling.upLeft = Vector3(28, 13, 7)
        ceiling.upRight = Vector3(28, 15, 7)
        ceiling.frontNormal = Geometry.rotatePoint(
            ceiling.downLeft.getDirectionTo(ceiling.upLeft).getNormalized(), Vector3(0, 1, 0), CommonConstants.axisOrigin, -Math.piHalf
        )
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)
        self.builder.buildRoundLamp(Vector3(29, 14, 6), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)

    def makeJoinLines(self):
        # main room
        self.addJoinLine(LevelSegmentJoinLine(Vector3(16, 14, 4), Vector3(28, 14, 4), Vector3(0, 0, -1)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(16, 13, 0), Vector3(16, 15, 0), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(21, 8, 0), Vector3(23, 8, 0), Vector3(0, 1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(28, 13, 4.2), Vector3(28, 15, 4.2), Vector3(-1, 0, 0)))
        # left room
        self.addJoinLine(LevelSegmentJoinLine(Vector3(14, 13, 0), Vector3(14, 15, 0), Vector3(-1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(11, 10, 0), Vector3(12, 10, 0), Vector3(0, 1, 0)))
        # bottom room
        self.addJoinLine(LevelSegmentJoinLine(Vector3(16, 3, 0), Vector3(16, 4, 0), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(21, 6, 0), Vector3(23, 6, 0), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(28, 3, 0), Vector3(28, 4, 0), Vector3(-1, 0, 0)))
        # left bottom pass
        self.addJoinLine(LevelSegmentJoinLine(Vector3(11, 6, 0), Vector3(12, 6, 0), Vector3(0, 1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(14, 3, 0), Vector3(14, 4, 0), Vector3(-1, 0, 0)))
        # right pass
        self.addJoinLine(LevelSegmentJoinLine(Vector3(30, 4.5, 0), Vector3(32, 4.5, 0), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(30, 6.5, 2), Vector3(32, 6.5, 2), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(30, 13, 3), Vector3(30, 15, 3), Vector3(1, 0, 0)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp
        # main room
        yield SplitPlane(Vector3(16, 14, 6.4), Vector3(0, 0, -1))
        yield SplitPlane(Vector3(16, 14, 2.2), Vector3(0, 0, -1))
        yield SplitPlane(Vector3(22, 11, 4.2), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(22, 17, 4.2), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(18, 14, 4.2), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(26, 14, 4.2), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(19, 18, 4.2), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(25, 18, 4.2), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(25.5, 17.5, 4.2), Vector3(1, 1, 0).getNormalized())
        yield SplitPlane(Vector3(18.5, 17.5, 4.2), Vector3(-1, 1, 0).getNormalized())
        yield SplitPlane(Vector3(19, 10, 4.2), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(25, 10, 4.2), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(18.5, 10.5, 4.2), Vector3(-1, -1, 0).getNormalized())
        yield SplitPlane(Vector3(25.5, 10.5, 4.2), Vector3(1, -1, 0).getNormalized())
        # left room
        yield SplitPlane(Vector3(12, 14, 2.2), Vector3(0, 0, -1))
        # bottom room
        yield SplitPlane(Vector3(22, 4, 2.2), Vector3(0, 0, -1))
        # left room pass
        yield SplitPlane(Vector3(15, 13, 0), Vector3(0, 1, 0))

    def getVisibilitySplitPlanes(self):
        # main room
        yield SplitPlane(Vector3(16, 14, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(28, 14, 0), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(22, 8, 0), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(16, 14, 4), Vector3(0, 0, -1))
        # left room
        yield SplitPlane(Vector3(14, 14, 0), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(11.5, 10, 0), Vector3(0, 1, 0))
        # bottom room
        yield SplitPlane(Vector3(22, 6, 0), Vector3(0, -1, 0))
        # left bottom pass
        yield SplitPlane(Vector3(11.5, 6, 0), Vector3(0, 1, 0))
        # right pass
        yield SplitPlane(Vector3(31, 4.5, 0), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(31, 6.5, 0), Vector3(0, 1, 0))
        yield SplitPlane(Vector3(30, 14, 0), Vector3(1, 0, 0))

    def getPlayerPosition(self):
        return Vector3(22, 14, 0)

    def getPlayerFrontNormal(self):
        return Vector3(-1, 0, 0)

    def getEnemyPositions(self):
        return []
