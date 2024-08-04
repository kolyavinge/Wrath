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


class LevelLoop(Level):

    def __init__(self):
        super().__init__()

        wall = Wall()
        wall.startPoint = Vector3(20, 20, 0)
        wall.endPoint = Vector3(65, 20, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(65, 20, 0)
        wall.endPoint = Vector3(70, 25, 0)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = wall.endPoint.getDirectionTo(wall.startPoint)
        wall.frontNormal = Geometry.rotatePoint(wall.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        wall.frontNormal.normalize()
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
        wall.startPoint = Vector3(70, 25, 0)
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

        floor = Stair()
        floor.downLeft = Vector3(50, 40, 3.1)
        floor.downRight = Vector3(60, 40, 0)
        floor.upLeft = Vector3(50, 50, 3.1)
        floor.upRight = Vector3(60, 50, 0)
        floor.leftFrontNormal = Vector3(1, 0, 0)
        floor.rightFrontNormal = Vector3(-1, 0, 0)
        floor.upFrontNormal = Vector3(0, -1, 0)
        floor.downFrontNormal = Vector3(0, 1, 0)
        floor.startBasePoint = Vector3(60, 40, 0)
        floor.endBasePoint = Vector3(50, 40, 3.1)
        floor.stepsCount = 6
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
        rightDirection = floor.downLeft.getDirectionTo(floor.downRight)
        rightDirection.normalize()
        floor.upNormal = Geometry.rotatePoint(rightDirection, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
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

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(10, 20, 3)
        ceiling.downRight = Vector3(70, 20, 3)
        ceiling.upLeft = Vector3(10, 30, 3)
        ceiling.upRight = Vector3(70, 30, 3)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(60, 30, 3)
        ceiling.downRight = Vector3(70, 30, 3)
        ceiling.upLeft = Vector3(60, 50, 3)
        ceiling.upRight = Vector3(70, 50, 3)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(50, 40, 6.1)
        ceiling.downRight = Vector3(60, 40, 3)
        ceiling.upLeft = Vector3(50, 50, 6.1)
        ceiling.upRight = Vector3(60, 50, 3)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(40, 5, 6.1)
        ceiling.downRight = Vector3(50, 5, 6.1)
        ceiling.upLeft = Vector3(40, 50, 6.1)
        ceiling.upRight = Vector3(50, 50, 6.1)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(20, 5, 3)
        ceiling.downRight = Vector3(40, 5, 6.1)
        ceiling.upLeft = Vector3(20, 15, 3)
        ceiling.upRight = Vector3(40, 15, 6.1)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(10, 5, 3)
        ceiling.downRight = Vector3(20, 5, 3)
        ceiling.upLeft = Vector3(10, 20, 3)
        ceiling.upRight = Vector3(20, 20, 3)
        ceiling.frontNormal = Vector3(0, 0, -1)
        self.addCeiling(ceiling)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(60, 30, 1.5)
        joinLine.endPoint = Vector3(70, 30, 1.5)
        joinLine.frontNormal = Vector3(0, 1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(60, 40, 1.5)
        joinLine.endPoint = Vector3(70, 40, 1.5)
        joinLine.frontNormal = Vector3(0, 1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(60, 40, 1.5)
        joinLine.endPoint = Vector3(60, 50, 1.5)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(50, 40, 4.6)
        joinLine.endPoint = Vector3(50, 50, 4.6)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(60, 40, 3.1)
        joinLine.endPoint = Vector3(60, 50, 3.1)
        joinLine.frontNormal = Vector3(0, 0, -1)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(40, 5, 4.6)
        joinLine.endPoint = Vector3(40, 15, 4.6)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(20, 5, 1.5)
        joinLine.endPoint = Vector3(20, 15, 1.5)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(20, 5, 3.5)
        joinLine.endPoint = Vector3(20, 15, 3.5)
        joinLine.frontNormal = Vector3(0, 0, -1)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(40, 5, 3.1)
        joinLine.endPoint = Vector3(40, 15, 3.1)
        joinLine.frontNormal = Vector3(0, 0, -1)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(20, 20, 1.5)
        joinLine.endPoint = Vector3(20, 30, 1.5)
        joinLine.frontNormal = Vector3(1, 0, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(10, 20, 1.5)
        joinLine.endPoint = Vector3(20, 20, 1.5)
        joinLine.frontNormal = Vector3(0, 1, 0)
        self.addJoinLine(joinLine)

        joinLine = LevelSegmentJoinLine()
        joinLine.startPoint = Vector3(50, 40, 3.1)
        joinLine.endPoint = Vector3(50, 50, 3.1)
        joinLine.frontNormal = Vector3(0, 0, -1)
        self.addJoinLine(joinLine)

        self.playerPosition = Vector3(25, 25, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)
