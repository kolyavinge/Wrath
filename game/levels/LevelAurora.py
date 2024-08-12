from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitLine import SplitLine
from game.engine.bsp.SplitPlane import SplitPlane
from game.lib.Math import Math
from game.model.level.Ceiling import Ceiling
from game.model.level.FlatFloor import FlatFloor
from game.model.level.Level import Level
from game.model.level.LevelSegmentJoinLine import LevelSegmentJoinLine
from game.model.level.Orientation import Orientation
from game.model.level.PlaneFloor import PlaneFloor
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall


class LevelAurora(Level):

    def __init__(self):
        super().__init__()
        self.makeRoom1()
        self.makeRoom2()
        self.makeRoom3()
        self.makePass1()
        self.makePass2()
        self.makePass3()
        self.makePass4()
        self.makePass5()
        self.makeJoinLines()
        self.setPlayerPosition()

    def makeRoom1(self):
        wallHeight = 12
        z = 0

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(70, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(90, 10, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 10, z)
        wall.endPoint = Vector3(130, 10, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 10, z)
        wall.endPoint = Vector3(150, 30, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 30, z)
        wall.endPoint = Vector3(150, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 40, 3)
        wall.endPoint = Vector3(150, 50, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight - 3
        wall.checkSegmentVisibility = False
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 50, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 80, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 80, z)
        wall.endPoint = Vector3(130, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 80, 3)
        wall.endPoint = Vector3(110, 80, 3)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight - 3
        wall.checkSegmentVisibility = False
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 80, z)
        wall.endPoint = Vector3(100, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 60, z)
        wall.endPoint = Vector3(90, 80, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 40, z)
        wall.endPoint = Vector3(70, 50, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = 8
        wall.checkSegmentVisibility = False
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 50, z)
        wall.endPoint = Vector3(70, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 1"
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(70, 10, z)
        floor.downRight = Vector3(150, 10, z)
        floor.upLeft = Vector3(70, 80, z)
        floor.upRight = Vector3(150, 80, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

        # second floor

        z = 8

        floor = FlatFloor()
        floor.downLeft = Vector3(70, 30, z)
        floor.downRight = Vector3(80, 30, z)
        floor.upLeft = Vector3(70, 60, z)
        floor.upRight = Vector3(80, 60, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(90, 10, z)
        floor.downRight = Vector3(90, 20, z)
        floor.upLeft = Vector3(70, 30, z)
        floor.upRight = Vector3(80, 30, z)
        floor.leftFrontNormal = Vector3(1, 1, 0)
        floor.leftFrontNormal.normalize()
        floor.rightFrontNormal = Vector3(-1, -1, 0)
        floor.rightFrontNormal.normalize()
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(90, 10, z)
        floor.downRight = Vector3(130, 10, z)
        floor.upLeft = Vector3(90, 20, z)
        floor.upRight = Vector3(130, 20, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(130, 10, z)
        floor.downRight = Vector3(150, 30, z)
        floor.upLeft = Vector3(130, 20, z)
        floor.upRight = Vector3(140, 30, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(-1, 1, 0)
        floor.upFrontNormal.normalize()
        floor.downFrontNormal = Vector3(-1, -1, 0)
        floor.downFrontNormal.normalize()
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(140, 30, z)
        floor.downRight = Vector3(150, 30, z)
        floor.upLeft = Vector3(140, 60, z)
        floor.upRight = Vector3(150, 60, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(140, 60, z)
        floor.downRight = Vector3(150, 60, z)
        floor.upLeft = Vector3(130, 70, z)
        floor.upRight = Vector3(130, 80, z)
        floor.leftFrontNormal = Vector3(-1, -1, 0)
        floor.leftFrontNormal.normalize()
        floor.rightFrontNormal = Vector3(1, 1, 0)
        floor.rightFrontNormal.normalize()
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(90, 70, z)
        floor.downRight = Vector3(130, 70, z)
        floor.upLeft = Vector3(90, 80, z)
        floor.upRight = Vector3(130, 80, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(70, 60, z)
        floor.downRight = Vector3(80, 60, z)
        floor.upLeft = Vector3(90, 80, z)
        floor.upRight = Vector3(90, 70, z)
        floor.leftFrontNormal = Vector3(1, -1, 0)
        floor.leftFrontNormal.normalize()
        floor.rightFrontNormal = Vector3(-1, -1, 0)
        floor.rightFrontNormal.normalize()
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

    def makeRoom2(self):
        wallHeight = 12
        z = 3

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(170, 120, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(190, 90, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 90, z)
        wall.endPoint = Vector3(210, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 90, 6)
        wall.endPoint = Vector3(220, 90, 6)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight - 3
        wall.checkSegmentVisibility = False
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 90, z)
        wall.endPoint = Vector3(250, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 90, z)
        wall.endPoint = Vector3(270, 110, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(270, 110, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 160, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 160, z)
        wall.endPoint = Vector3(250, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 160, z)
        wall.endPoint = Vector3(240, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = 9
        wall.checkSegmentVisibility = False
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 160, z)
        wall.endPoint = Vector3(230, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 140, z)
        wall.endPoint = Vector3(190, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 130, z)
        wall.endPoint = Vector3(170, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 120, 6)
        wall.endPoint = Vector3(170, 130, 6)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight - 3
        wall.checkSegmentVisibility = False
        wall.info = "room 2"
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(170, 90, z)
        floor.downRight = Vector3(270, 90, z)
        floor.upLeft = Vector3(170, 160, z)
        floor.upRight = Vector3(270, 160, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        # second floor

        z = 12

        floor = FlatFloor()
        floor.downLeft = Vector3(230, 90, z)
        floor.downRight = Vector3(240, 90, z)
        floor.upLeft = Vector3(230, 160, z)
        floor.upRight = Vector3(240, 160, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(200, 90, z)
        floor.downRight = Vector3(210, 90, z)
        floor.upLeft = Vector3(200, 160, z)
        floor.upRight = Vector3(210, 160, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(210, 120, z)
        floor.downRight = Vector3(230, 120, z)
        floor.upLeft = Vector3(210, 130, z)
        floor.upRight = Vector3(230, 130, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

    def makeRoom3(self):
        wallHeight = 4
        z = 0

        wall = Wall()
        wall.startPoint = Vector3(70, 100, z)
        wall.endPoint = Vector3(70, 110, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 100, z)
        wall.endPoint = Vector3(100, 100, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 100, z)
        wall.endPoint = Vector3(110, 120, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 120, z)
        wall.endPoint = Vector3(140, 120, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 130, z)
        wall.endPoint = Vector3(140, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 160, z)
        wall.endPoint = Vector3(130, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 150, z)
        wall.endPoint = Vector3(100, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 130, z)
        wall.endPoint = Vector3(90, 150, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 130, z)
        wall.endPoint = Vector3(90, 130, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 120, z)
        wall.endPoint = Vector3(70, 130, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.info = "room 3"
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(70, 100, z)
        floor.downRight = Vector3(110, 100, z)
        floor.upLeft = Vector3(70, 130, z)
        floor.upRight = Vector3(110, 130, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(90, 130, z)
        floor.downRight = Vector3(140, 130, z)
        floor.upLeft = Vector3(90, 160, z)
        floor.upRight = Vector3(140, 160, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(110, 120, z)
        floor.downRight = Vector3(140, 120, z)
        floor.upLeft = Vector3(110, 130, z)
        floor.upRight = Vector3(140, 130, z)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = z
        self.addFloor(floor)

    def makePass1(self):
        wall = Wall()
        wall.startPoint = Vector3(150, 40, 0)
        wall.endPoint = Vector3(190, 40, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 40, 2)
        wall.endPoint = Vector3(220, 70, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 70, 2)
        wall.endPoint = Vector3(220, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 50, 0)
        wall.endPoint = Vector3(190, 50, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 50, 2)
        wall.endPoint = Vector3(210, 70, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 70, 2)
        wall.endPoint = Vector3(210, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 1"
        self.addWall(wall)

        floor = PlaneFloor()
        floor.downLeft = Vector3(150, 40, 0)
        floor.downRight = Vector3(190, 40, 2)
        floor.upLeft = Vector3(150, 50, 0)
        floor.upRight = Vector3(190, 50, 2)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.upRight.copy()
        v.sub(floor.upLeft)
        floor.upNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(190, 40, 2)
        floor.downRight = Vector3(220, 40, 2)
        floor.upLeft = Vector3(190, 70, 2)
        floor.upRight = Vector3(220, 70, 2)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 2
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(210, 70, 2)
        floor.downRight = Vector3(220, 70, 2)
        floor.upLeft = Vector3(210, 90, 3)
        floor.upRight = Vector3(220, 90, 3)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.upRight.copy()
        v.sub(floor.downRight)
        floor.upNormal = Geometry.rotatePoint(v, Vector3(1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

    def makePass2(self):
        wall = Wall()
        wall.startPoint = Vector3(40, 120, 4)
        wall.endPoint = Vector3(50, 120, 4)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 120, 4)
        wall.endPoint = Vector3(70, 120, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 40, 4)
        wall.endPoint = Vector3(40, 120, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 40, 4)
        wall.endPoint = Vector3(50, 40, 4)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 40, 4)
        wall.endPoint = Vector3(70, 40, 8)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 110, 4)
        wall.endPoint = Vector3(70, 110, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 50, 4)
        wall.endPoint = Vector3(50, 110, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 50, 4)
        wall.endPoint = Vector3(70, 50, 8)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 2"
        self.addWall(wall)

        stair = Stair()
        stair.downLeft = Vector3(50, 110, 4)
        stair.downRight = Vector3(70, 110, 0)
        stair.upLeft = Vector3(50, 120, 4)
        stair.upRight = Vector3(70, 120, 0)
        stair.leftFrontNormal = Vector3(1, 0, 0)
        stair.rightFrontNormal = Vector3(-1, 0, 0)
        stair.upFrontNormal = Vector3(0, -1, 0)
        stair.downFrontNormal = Vector3(0, 1, 0)
        stair.startBasePoint = Vector3(70, 110, 0)
        stair.endBasePoint = Vector3(50, 110, 4)
        stair.stepsCount = 8
        stair.commit()
        self.addFloor(stair)

        floor = FlatFloor()
        floor.downLeft = Vector3(40, 40, 4)
        floor.downRight = Vector3(50, 40, 4)
        floor.upLeft = Vector3(40, 120, 4)
        floor.upRight = Vector3(50, 120, 4)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 4
        self.addFloor(floor)

        stair = Stair()
        stair.downLeft = Vector3(50, 40, 4)
        stair.downRight = Vector3(70, 40, 8)
        stair.upLeft = Vector3(50, 50, 4)
        stair.upRight = Vector3(70, 50, 8)
        stair.leftFrontNormal = Vector3(1, 0, 0)
        stair.rightFrontNormal = Vector3(-1, 0, 0)
        stair.upFrontNormal = Vector3(0, -1, 0)
        stair.downFrontNormal = Vector3(0, 1, 0)
        stair.startBasePoint = Vector3(50, 50, 4)
        stair.endBasePoint = Vector3(70, 50, 8)
        stair.stepsCount = 8
        stair.debug = True
        stair.commit()
        self.addFloor(stair)

    def makePass3(self):
        wall = Wall()
        wall.startPoint = Vector3(130, 160, 0)
        wall.endPoint = Vector3(130, 170, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 170, 1)
        wall.endPoint = Vector3(130, 180, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 180, 1)
        wall.endPoint = Vector3(140, 180, 1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 180, 1)
        wall.endPoint = Vector3(240, 180, 12)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 160, 12)
        wall.endPoint = Vector3(240, 180, 12)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 160, 0)
        wall.endPoint = Vector3(140, 170, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 170, 1)
        wall.endPoint = Vector3(230, 170, 12)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 160, 12)
        wall.endPoint = Vector3(230, 170, 12)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 3"
        self.addWall(wall)

        floor = PlaneFloor()
        floor.downLeft = Vector3(130, 160, 0)
        floor.downRight = Vector3(140, 160, 0)
        floor.upLeft = Vector3(130, 170, 1)
        floor.upRight = Vector3(140, 170, 1)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.downRight.getDirectionTo(floor.upRight)
        floor.upNormal = Geometry.rotatePoint(v, Vector3(1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(130, 170, 1)
        floor.downRight = Vector3(140, 170, 1)
        floor.upLeft = Vector3(130, 180, 1)
        floor.upRight = Vector3(140, 180, 1)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 1
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(140, 170, 1)
        floor.downRight = Vector3(230, 170, 12)
        floor.upLeft = Vector3(140, 180, 1)
        floor.upRight = Vector3(230, 180, 12)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.upLeft.getDirectionTo(floor.upRight)
        floor.upNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(230, 160, 12)
        floor.downRight = Vector3(240, 160, 12)
        floor.upLeft = Vector3(230, 180, 12)
        floor.upRight = Vector3(240, 180, 12)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 12
        self.addFloor(floor)

    def makePass4(self):
        wall = Wall()
        wall.startPoint = Vector3(140, 130, 0)
        wall.endPoint = Vector3(170, 130, 3)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.info = "pass 4"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 120, 0)
        wall.endPoint = Vector3(170, 120, 3)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.info = "pass 4"
        self.addWall(wall)

        floor = PlaneFloor()
        floor.downLeft = Vector3(140, 120, 0)
        floor.downRight = Vector3(170, 120, 3)
        floor.upLeft = Vector3(140, 130, 0)
        floor.upRight = Vector3(170, 130, 3)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.upLeft.getDirectionTo(floor.upRight)
        floor.upNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

    def makePass5(self):
        wall = Wall()
        wall.startPoint = Vector3(100, 80, 0)
        wall.endPoint = Vector3(100, 100, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.info = "pass 5"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 80, 0)
        wall.endPoint = Vector3(110, 100, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.info = "pass 5"
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(100, 80, 0)
        floor.downRight = Vector3(110, 80, 0)
        floor.upLeft = Vector3(100, 100, 0)
        floor.upRight = Vector3(110, 100, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

    def getSplitLines(self):
        result = []

        s = SplitLine()
        s.startPoint = Vector3(0, 80, 0)
        s.endPoint = Vector3(300, 80, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(0, 90, 0)
        s.endPoint = Vector3(300, 90, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(150, 0, 0)
        s.endPoint = Vector3(150, 80, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(70, 0, 0)
        s.endPoint = Vector3(70, 80, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(0, 160, 0)
        s.endPoint = Vector3(300, 160, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(170, 90, 0)
        s.endPoint = Vector3(170, 160, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(70, 90, 0)
        s.endPoint = Vector3(70, 160, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitLine()
        s.startPoint = Vector3(140, 90, 0)
        s.endPoint = Vector3(140, 160, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        i = 0
        while i < len(result):
            result[i].priority = i
            i += 1

        return result

    def getCollisionSplitPlanes(self):
        result = []

        result.extend(self.getVisibilitySplitPlanes())

        # room 1
        s = SplitPlane()
        s.basePoint = Vector3(110, 50, 3)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 45, 8)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(90, 45, 8)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 45, 8)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 30, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 60, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(85, 25, 8)
        s.frontNormal = Vector3(-1, -1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(85, 65, 8)
        s.frontNormal = Vector3(-1, 1, 0)
        s.frontNormal.normalize()
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(130, 45, 8)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 45, 8)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 30, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 60, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(135, 25, 8)
        s.frontNormal = Vector3(1, -1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(135, 65, 8)
        s.frontNormal = Vector3(1, 1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 20, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 70, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 40, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 50, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        # pass 5
        s = SplitPlane()
        s.basePoint = Vector3(100, 85, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 85, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(105, 100, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # pass 1
        s = SplitPlane()
        s.basePoint = Vector3(190, 45, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(215, 70, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        # room 2
        s = SplitPlane()
        s.basePoint = Vector3(210, 120, 6)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(200, 125, 12)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(210, 125, 12)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(230, 125, 12)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(240, 125, 12)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 130, 12)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 120, 12)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # room 3
        s = SplitPlane()
        s.basePoint = Vector3(110, 130, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 125, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        # pass 2
        s = SplitPlane()
        s.basePoint = Vector3(50, 115, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(50, 45, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        # pass 3
        s = SplitPlane()
        s.basePoint = Vector3(180, 170, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 165, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 175, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(230, 175, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        return result

    def getVisibilitySplitPlanes(self):
        result = []

        s = SplitPlane()
        s.basePoint = Vector3(150, 80, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 90, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 50, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(70, 50, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 160, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(170, 120, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(70, 120, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 120, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        return result

    def makeJoinLines(self):
        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(100, 80, 2)
        joinLine.endPoint = Vector3(110, 80, 2)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(210, 80, 4)
        joinLine.endPoint = Vector3(220, 80, 4)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(40, 80, 5)
        joinLine.endPoint = Vector3(50, 80, 5)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(150, 40, 2)
        joinLine.endPoint = Vector3(150, 50, 2)
        joinLine.frontNormal = Vector3(-1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(70, 40, 10)
        joinLine.endPoint = Vector3(70, 50, 10)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(100, 90, 2)
        joinLine.endPoint = Vector3(110, 90, 2)
        joinLine.frontNormal = Vector3(0, 1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(40, 90, 5)
        joinLine.endPoint = Vector3(50, 90, 5)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(210, 90, 2)
        joinLine.endPoint = Vector3(220, 90, 2)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(130, 160, 2)
        joinLine.endPoint = Vector3(140, 160, 2)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(230, 160, 13)
        joinLine.endPoint = Vector3(240, 160, 13)
        joinLine.frontNormal = Vector3(0, -1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(170, 120, 4)
        joinLine.endPoint = Vector3(170, 130, 4)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(70, 110, 2)
        joinLine.endPoint = Vector3(70, 120, 2)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(140, 120, 2)
        joinLine.endPoint = Vector3(140, 130, 2)
        joinLine.frontNormal = Vector3(-1, 0, 0)
        self.addJoinLine(joinLine)

    def setPlayerPosition(self):
        self.playerPosition = Vector3(75, 45, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)
