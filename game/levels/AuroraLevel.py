from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.levels.builder.CeilingBuilder import CeilingHole
from game.levels.builder.Doorway import Doorway
from game.levels.builder.DoorwayBorder import DoorwayBorder
from game.levels.builder.LevelBuilder import LevelBuilder
from game.levels.builder.WallBorder import WallBorder
from game.levels.builder.WallInfo import WallInfo
from game.model.level.Level import Level
from game.model.level.PowerupArea import PowerupArea
from game.model.Material import Material


class AuroraLevel(Level):

    def __init__(self):
        super().__init__()
        self.builder = LevelBuilder(self)
        self.makeMainRoom()
        self.setPlayerPosition()

    def makeMainRoom(self):
        self.builder.buildWalls(
            Vector3(16, 11, 0),
            WallInfo(
                Vector3(16, 17, 0),
                Vector3(1, 0, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(16, 13, 0), 2, 2.5, Material.floorMetal3, DoorwayBorder(0.3, 0.1, Material.ceilingMetal2)),
            ),
            WallInfo(
                Vector3(19, 20, 0),
                Vector3(1, -1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 20, 0),
                Vector3(0, -1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 17, 0),
                Vector3(-1, -1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(28, 11, 0),
                Vector3(-1, 0, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(25, 8, 0),
                Vector3(-1, 1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(19, 8, 0),
                Vector3(0, 1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(16, 11, 0),
                Vector3(1, 1, 0),
                4,
                Material.wallMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
        )
        # self.builder.buildPillar(Vector3(4, 3, 0), 0.5, 3, Material.ceilingMetal1)
        self.builder.buildFlatFloor(Vector3(16, 8, 0), 12, 12, Material.floorConcrete1)
        self.builder.buildCeiling(Vector3(16, 8, 4), 12, 12, Material.floorMetal2, CeilingHole(3, 3, Material.floorMetal2))
        # self.builder.buildRoundLamp(Vector3(1, 3, 3), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)
        # self.builder.buildRectLamp(Vector3(4, 3, 3), Vector3(0, 0, -1), 0.05, 0.1, 1.0, Vector3(1, 0, 0), Material.ceilingMetal2)
        self.builder.buildLight(Vector3(22, 14, 4))
        self.addPowerupArea(PowerupArea(Vector3(22, 14, 0), Vector3(22, 14, 0), 6))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        # yield SplitPlane(Vector3(0, 2, 0), Vector3(1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(16, 14, 0), Vector3(1, 0, 0))
        # yield SplitPlane(Vector3(6, 3, 0), Vector3(-1, 0, 0))
        # yield SplitPlane(Vector3(3, 6, 0), Vector3(0, -1, 0))
        # yield SplitPlane(Vector3(3, 1, 0), Vector3(0, 1, 0))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(19, 13, 0)
        self.playerFrontNormal = Vector3(0, 1, 0)
