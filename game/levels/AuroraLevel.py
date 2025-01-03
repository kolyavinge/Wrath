from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.levels.builder.CeilingBuilder import CeilingHole
from game.levels.builder.Doorway import Doorway
from game.levels.builder.DoorwayBorder import DoorwayBorder
from game.levels.builder.LevelBuilder import LevelBuilder
from game.levels.builder.WallBorder import WallBorder
from game.levels.builder.WallInfo import WallInfo
from game.model.level.Level import Level
from game.model.level.LevelSegmentJoinLine import LevelSegmentJoinLine
from game.model.level.PowerupArea import PowerupArea
from game.model.Material import Material


class AuroraLevel(Level):

    def __init__(self):
        super().__init__()
        self.builder = LevelBuilder(self)
        self.makeMainRoom()
        self.makeJoinLines()
        self.setPlayerPosition()

    def makeMainRoom(self):
        # first floor
        firstFloorHeight = 4
        self.builder.buildWalls(
            Vector3(16, 11, 0),
            WallInfo(
                Vector3(16, 17, 0),
                Vector3(1, 0, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(16, 13, 0), 2, 2.5, Material.floorMetal3, DoorwayBorder(0.3, 0.1, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(19, 20, 0),
                Vector3(1, -1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 20, 0),
                Vector3(0, -1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 17, 0),
                Vector3(-1, -1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 11, 0),
                Vector3(-1, 0, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 8, 0),
                Vector3(-1, 1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 8, 0),
                Vector3(0, 1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(16, 11, 0),
                Vector3(1, 1, 0),
                firstFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        # balcony
        balconyHeight = 0.2
        balconyZ = firstFloorHeight + balconyHeight
        self.builder.buildBalcony(
            Vector3(16, 17, balconyZ),
            Vector3(16, 11, balconyZ),
            Vector3(17, 17, balconyZ),
            Vector3(17, 11, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(28, 11, balconyZ),
            Vector3(28, 17, balconyZ),
            Vector3(27, 11, balconyZ),
            Vector3(27, 17, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(19, 20, balconyZ),
            Vector3(25, 20, balconyZ),
            Vector3(19, 19, balconyZ),
            Vector3(25, 19, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(19, 8, balconyZ),
            Vector3(25, 8, balconyZ),
            Vector3(19, 9, balconyZ),
            Vector3(25, 9, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(16, 11, balconyZ),
            Vector3(19, 8, balconyZ),
            Vector3(17, 11, balconyZ),
            Vector3(19, 9, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(19, 20, balconyZ),
            Vector3(16, 17, balconyZ),
            Vector3(19, 19, balconyZ),
            Vector3(17, 17, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(28, 17, balconyZ),
            Vector3(25, 20, balconyZ),
            Vector3(27, 17, balconyZ),
            Vector3(25, 19, balconyZ),
            balconyHeight,
            Material.floorMetal2,
            Material.edgeMetal1,
        )
        self.builder.buildBalcony(
            Vector3(25, 8, balconyZ),
            Vector3(28, 11, balconyZ),
            Vector3(25, 9, balconyZ),
            Vector3(27, 11, balconyZ),
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
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 20, balconyZ),
                Vector3(1, -1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 20, balconyZ),
                Vector3(0, -1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 17, balconyZ),
                Vector3(-1, -1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 11, balconyZ),
                Vector3(-1, 0, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 8, balconyZ),
                Vector3(-1, 1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 8, balconyZ),
                Vector3(0, 1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(16, 11, balconyZ),
                Vector3(1, 1, 0),
                secondFloorHeight,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        # self.builder.buildPillar(Vector3(4, 3, 0), 0.5, 3, Material.ceilingMetal1)
        self.builder.buildFlatFloor(Vector3(16, 8, 0), 12, 12, Material.floorConcrete1)
        ceilingZ = balconyZ + secondFloorHeight
        self.builder.buildCeiling(Vector3(16, 8, ceilingZ), 12, 12, Material.ceilingMetal1, CeilingHole(4, 4))
        self.builder.buildLight(Vector3(22, 14, 4), "mainRoom")
        self.builder.buildLight(Vector3(22, 14, ceilingZ), "mainRoom")
        self.addPowerupArea(PowerupArea(Vector3(22, 14, 0), Vector3(22, 14, 0), 6))

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(16, 14, 4), Vector3(28, 14, 4), Vector3(0, 0, -1)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        # yield SplitPlane(Vector3(0, 2, 0), Vector3(1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(16, 14, 4), Vector3(0, 0, -1))
        yield SplitPlane(Vector3(16, 14, 0), Vector3(1, 0, 0))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(19, 13, 0)
        self.playerFrontNormal = Vector3(0, 1, 0)
