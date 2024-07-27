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
        self.makeRoom2()
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

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(70, 60, 2)
        joinLine.endPoint = Vector3(150, 60, 2)
        joinLine.frontNormal = Vector3(0, 1, 0)
        joinLine.commit()
        self.addJoinLine(joinLine)

    def makePass1(self):
        wall = Wall()
        wall.startPoint = Vector3(150, 50, 0)
        wall.endPoint = Vector3(180, 50, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(180, 50, 2)
        wall.endPoint = Vector3(220, 80, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Geometry.rotatePoint(Vector3(4, 3, 0), CommonConstants.zAxis, CommonConstants.axisOrigin, Math.piHalf)
        wall.frontNormal.normalize()
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 80, 2)
        wall.endPoint = Vector3(220, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 60, 0)
        wall.endPoint = Vector3(180, 60, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(180, 60, 2)
        wall.endPoint = Vector3(210, 80, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Geometry.rotatePoint(Vector3(3, 2, 0), CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        wall.frontNormal.normalize()
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 80, 2)
        wall.endPoint = Vector3(210, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        self.addWall(wall)

        floor = PlaneFloor()
        floor.downLeft = Vector3(150, 50, 0)
        floor.downRight = Vector3(180, 50, 2)
        floor.upLeft = Vector3(150, 60, 0)
        floor.upRight = Vector3(180, 60, 2)
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
        floor.downLeft = Vector3(180, 50, 2)
        floor.downRight = Vector3(220, 50, 2)
        floor.upLeft = Vector3(180, 80, 2)
        floor.upRight = Vector3(220, 80, 2)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 2
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(210, 80, 2)
        floor.downRight = Vector3(220, 80, 2)
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

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(150, 50, 2)
        joinLine.endPoint = Vector3(150, 60, 2)
        joinLine.frontNormal = Vector3(-1, 0, 0)
        joinLine.commit()
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(180, 50, 3)
        joinLine.endPoint = Vector3(180, 60, 3)
        joinLine.frontNormal = Vector3(-1, 0, 0)
        joinLine.commit()
        self.addJoinLine(joinLine)

    def makeRoom2(self):
        wallHeight = 12
        z = 3

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(170, 120, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(190, 90, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 90, z)
        wall.endPoint = Vector3(210, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 90, z)
        wall.endPoint = Vector3(250, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 90, z)
        wall.endPoint = Vector3(270, 110, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(270, 110, z)
        wall.endPoint = Vector3(270, 140, z)
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
        wall.startPoint = Vector3(250, 160, z)
        wall.endPoint = Vector3(270, 140, z)
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
        wall.startPoint = Vector3(240, 160, z)
        wall.endPoint = Vector3(250, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 160, z)
        wall.endPoint = Vector3(230, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 140, z)
        wall.endPoint = Vector3(190, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 130, z)
        wall.endPoint = Vector3(170, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
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

    def setPlayerPosition(self):
        self.playerPosition = Vector3(140, 55, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)
