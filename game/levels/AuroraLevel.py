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
        self.makeRoom1()
        self.setPlayerPosition()

    def makeRoom1(self):
        self.builder.buildWalls(
            Vector3(1, 1, 0),
            WallInfo(
                Vector3(1, 5, 0),
                Vector3(1, 0, 0),
                3,
                Material.floorMetal4,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(6, 5, 0),
                Vector3(0, -1, 0),
                3,
                Material.floorMetal4,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(6, 1, 0),
                Vector3(-1, 0, 0),
                3,
                Material.ceilingMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
            ),
            WallInfo(
                Vector3(1, 1, 0),
                Vector3(0, 1, 0),
                3,
                Material.ceilingMetal1,
                WallBorder(0.2, 0.1, Material.ceilingMetal1, Material.ceilingMetal2),
                WallBorder(0.3, 0.2, Material.ceilingMetal1, Material.ceilingMetal2),
                Doorway(Vector3(4, 1, 0), 1, 2.2, Material.floorMetal3, DoorwayBorder(0.2, 0.1, Material.ceilingMetal2)),
            ),
        )
        # self.builder.buildPillar(Vector3(4, 3, 0), 0.5, 3, Material.ceilingMetal1)
        self.builder.buildFlatFloor(Vector3(1, 1, 0), 5, 4, Material.floorConcrete1)
        self.builder.buildCeiling(Vector3(1, 1, 3), 5, 4, Material.floorMetal2, CeilingHole(1, 2, Material.floorMetal2))
        self.builder.buildRoundLamp(Vector3(1, 3, 3), Vector3(0, 0, -1), 0.1, 0.05, Material.ceilingMetal2)
        # self.builder.buildRectLamp(Vector3(4, 3, 3), Vector3(0, 0, -1), 0.05, 0.1, 1.0, Vector3(1, 0, 0), Material.ceilingMetal2)
        self.addPowerupArea(PowerupArea(Vector3(2, 2.5, 0), Vector3(2, 2.5, 0), 0.5))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

        # yield SplitPlane(Vector3(0, 2, 0), Vector3(1, 0, 0))

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(1, 3, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(6, 3, 0), Vector3(-1, 0, 0))
        yield SplitPlane(Vector3(3, 6, 0), Vector3(0, -1, 0))
        yield SplitPlane(Vector3(3, 1, 0), Vector3(0, 1, 0))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(2, 2, 0)
        self.playerFrontNormal = Vector3(0, 1, 0)
