from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
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
        self.makePass1()
        self.setPlayerPosition()

    def makeRoom1(self):
        wallHeight = 12

        wall = Wall()
        wall.startPoint = Vector3(70, 40, 0)
        wall.endPoint = Vector3(70, 50, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 40, 0)
        wall.endPoint = Vector3(90, 20, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 20, 0)
        wall.endPoint = Vector3(130, 20, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 20, 0)
        wall.endPoint = Vector3(150, 40, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 40, 0)
        wall.endPoint = Vector3(150, 50, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 60, 0)
        wall.endPoint = Vector3(150, 70, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 90, 0)
        wall.endPoint = Vector3(150, 70, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 90, 0)
        wall.endPoint = Vector3(130, 90, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 90, 0)
        wall.endPoint = Vector3(100, 90, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 70, 0)
        wall.endPoint = Vector3(90, 90, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 60, 0)
        wall.endPoint = Vector3(70, 70, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(70, 20, 0)
        floor.downRight = Vector3(150, 20, 0)
        floor.upLeft = Vector3(70, 90, 0)
        floor.upRight = Vector3(150, 90, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

    def makePass1(self):
        wall = Wall()
        wall.startPoint = Vector3(150, 50, 0)
        wall.endPoint = Vector3(180, 50, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(180, 50, 0)
        wall.endPoint = Vector3(220, 80, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Geometry.rotatePoint(Vector3(4, 3, 0), CommonConstants.zAxis, CommonConstants.axisOrigin, Math.piHalf)
        wall.frontNormal.normalize()
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 80, 0)
        wall.endPoint = Vector3(220, 90, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 60, 0)
        wall.endPoint = Vector3(180, 60, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(180, 60, 0)
        wall.endPoint = Vector3(210, 80, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Geometry.rotatePoint(Vector3(3, 2, 0), CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        wall.frontNormal.normalize()
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 80, 0)
        wall.endPoint = Vector3(210, 90, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(150, 50, 0)
        floor.downRight = Vector3(180, 50, 0)
        floor.upLeft = Vector3(150, 60, 0)
        floor.upRight = Vector3(180, 60, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(180, 50, 0)
        floor.downRight = Vector3(220, 80, 2)
        floor.upLeft = Vector3(180, 60, 0)
        floor.upRight = Vector3(210, 80, 2)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        v = floor.upRight.copy()
        v.sub(floor.upLeft)
        n = Geometry.rotatePoint(Vector3(3, 2, 0), CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        n.normalize()
        floor.upNormal = Geometry.rotatePoint(v, n, CommonConstants.axisOrigin, Math.piHalf)
        floor.upNormal.normalize()
        floor.commit()
        self.addFloor(floor)

    def setPlayerPosition(self):
        self.playerPosition = Vector3(140, 55, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)
