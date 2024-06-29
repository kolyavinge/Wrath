from game.anx.Constants import Constants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.FlatFloor import FlatFloor
from game.model.level.Level import Level
from game.model.level.Orientation import Orientation
from game.model.level.PlaneFloor import PlaneFloor
from game.model.level.Wall import Wall


class LevelLoop(Level):

    def __init__(self):
        super().__init__()

        wall = Wall()
        wall.startPoint = Vector3(20, 20, 0)
        wall.endPoint = Vector3(70, 20, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(10, 30, 0)
        wall.endPoint = Vector3(60, 30, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(60, 30, 0)
        wall.endPoint = Vector3(60, 40, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 20, 0)
        wall.endPoint = Vector3(70, 50, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 40, 3.1)
        wall.endPoint = Vector3(60, 40, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(60, 50, 0)
        wall.endPoint = Vector3(70, 50, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 50, 3.1)
        wall.endPoint = Vector3(60, 50, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 50, 3.1)
        wall.endPoint = Vector3(50, 50, 3.1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 15, 3.1)
        wall.endPoint = Vector3(40, 50, 3.1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 5, 3.1)
        wall.endPoint = Vector3(50, 40, 3.1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(10, 5, 0)
        wall.endPoint = Vector3(20, 5, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(20, 5, 0)
        wall.endPoint = Vector3(40, 5, 3.1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 5, 3.1)
        wall.endPoint = Vector3(50, 5, 3.1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(20, 15, 0)
        wall.endPoint = Vector3(40, 15, 3.1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(10, 5, 0)
        wall.endPoint = Vector3(10, 30, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(20, 15, 0)
        wall.endPoint = Vector3(20, 20, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        self.addWall(wall)

        floor = FlatFloor()
        floor.downLeft = Vector3(10, 20, 0)
        floor.downRight = Vector3(70, 20, 0)
        floor.upLeft = Vector3(10, 30, 0)
        floor.upRight = Vector3(70, 30, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(60, 30, 0)
        floor.downRight = Vector3(70, 30, 0)
        floor.upLeft = Vector3(60, 50, 0)
        floor.upRight = Vector3(70, 50, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(50, 40, 3.1)
        floor.downRight = Vector3(60, 40, 0)
        floor.upLeft = Vector3(50, 50, 3.1)
        floor.upRight = Vector3(60, 50, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        leftDirection = floor.downLeft.getCopy()
        leftDirection.sub(floor.downRight)
        leftDirection.normalize()
        floor.upNormal = Geometry.rotatePoint(leftDirection, Vector3(0, 1, 0), Constants.axisOrigin, Math.piHalf)
        floor.commit()
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(40, 5, 3.1)
        floor.downRight = Vector3(50, 5, 3.1)
        floor.upLeft = Vector3(40, 50, 3.1)
        floor.upRight = Vector3(50, 50, 3.1)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 3.1
        self.addFloor(floor)

        floor = PlaneFloor()
        floor.downLeft = Vector3(20, 5, 0)
        floor.downRight = Vector3(40, 5, 3.1)
        floor.upLeft = Vector3(20, 15, 0)
        floor.upRight = Vector3(40, 15, 3.1)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        rightDirection = floor.downRight.getCopy()
        rightDirection.sub(floor.downLeft)
        rightDirection.normalize()
        floor.upNormal = Geometry.rotatePoint(rightDirection, Vector3(0, -1, 0), Constants.axisOrigin, Math.piHalf)
        floor.commit()
        self.addFloor(floor)

        floor = FlatFloor()
        floor.downLeft = Vector3(10, 5, 0)
        floor.downRight = Vector3(20, 5, 0)
        floor.upLeft = Vector3(10, 20, 0)
        floor.upRight = Vector3(20, 20, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.z = 0
        self.addFloor(floor)

        self.playerPosition = Vector3(25, 25, 0)

    def addWall(self, wall):
        self.walls.append(wall)

    def addFloor(self, floor):
        self.floors.append(floor)
