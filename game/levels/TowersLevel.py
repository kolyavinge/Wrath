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
        self.makeLeftTower()
        self.makeRightTower()
        self.makePasses()
        self.makeJoinLines()
        self.setPlayerPosition()

    def makeLeftTower(self):
        self.builder.buildLight(Vector3(1, 11, 10), 0.5, "mainLight")
        self.builder.buildFlatFloor(Vector3(0, 10, 0), 40, 40, Material.floorConcrete1)

    def makeRightTower(self):
        self.builder.buildLight(Vector3(101, 11, 10), 0.5, "mainLight")
        self.builder.buildFlatFloor(Vector3(100, 10, 0), 40, 40, Material.floorConcrete1)

    def makePasses(self):
        self.builder.buildLight(Vector3(40, 20, 10), 0.5, "mainLight")
        self.builder.buildFlatFloor(Vector3(40, 12, 0), 60, 5, Material.floorConcrete1)
        self.addPowerupArea(PowerupArea(Vector3(20, 18.5, 0), Vector3(21, 18.5, 0), 1))

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(40, 6, 0), Vector3(40, 26, 0), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 6, 0), Vector3(100, 26, 0), Vector3(1, 0, 0)))

    def getCollisionSplitPlanes(self):
        for sp in self.getVisibilitySplitPlanes():
            yield sp

    def getVisibilitySplitPlanes(self):
        yield SplitPlane(Vector3(40, 17, 0), Vector3(1, 0, 0))
        yield SplitPlane(Vector3(100, 17, 0), Vector3(1, 0, 0))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(1, 11, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)
