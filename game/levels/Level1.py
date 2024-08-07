from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.FlatFloor import FlatFloor
from game.model.level.Level import Level
from game.model.level.Orientation import Orientation
from game.model.level.PlaneFloor import PlaneFloor
from game.model.level.Wall import Wall


class Level1(Level):

    def __init__(self):
        super().__init__()

        wall1 = Wall()
        wall1.startPoint = Vector3(0, 0, 0)
        wall1.endPoint = Vector3(0, 10, 0)
        wall1.orientation = Orientation.vertical
        wall1.frontNormal = Vector3(1, 0, 0)
        wall1.commit()

        wall2 = Wall()
        wall2.startPoint = Vector3(0, 10, 0)
        wall2.endPoint = Vector3(20, 10, 0)
        wall2.orientation = Orientation.horizontal
        wall2.frontNormal = Vector3(0, -1, 0)
        wall2.commit()

        wall3 = Wall()
        wall3.startPoint = Vector3(20, 10, 0)
        wall3.endPoint = Vector3(20, 15, 0)
        wall3.orientation = Orientation.vertical
        wall3.frontNormal = Vector3(1, 0, 0)
        wall3.commit()

        wall4 = Wall()
        wall4.startPoint = Vector3(20, 15, 0)
        wall4.endPoint = Vector3(30, 15, 0)
        wall4.orientation = Orientation.horizontal
        wall4.frontNormal = Vector3(0, -1, 0)
        wall4.commit()

        wall5 = Wall()
        wall5.startPoint = Vector3(30, 5, 0)
        wall5.endPoint = Vector3(30, 15, 0)
        wall5.orientation = Orientation.vertical
        wall5.frontNormal = Vector3(-1, 0, 0)
        wall5.commit()

        wall6 = Wall()
        wall6.startPoint = Vector3(10, 5, 0)
        wall6.endPoint = Vector3(30, 5, 0)
        wall6.orientation = Orientation.horizontal
        wall6.frontNormal = Vector3(0, 1, 0)
        wall6.commit()

        wall7 = Wall()
        wall7.startPoint = Vector3(10, 0, 0)
        wall7.endPoint = Vector3(10, 5, 0)
        wall7.orientation = Orientation.vertical
        wall7.frontNormal = Vector3(-1, 0, 0)
        wall7.commit()

        wall8 = Wall()
        wall8.startPoint = Vector3(0, 0, 0)
        wall8.endPoint = Vector3(10, 0, 0)
        wall8.orientation = Orientation.horizontal
        wall8.frontNormal = Vector3(0, 1, 0)
        wall8.commit()

        # pole
        wall9 = Wall()
        wall9.startPoint = Vector3(2, 6, 0)
        wall9.endPoint = Vector3(2, 7, 0)
        wall9.orientation = Orientation.vertical
        wall9.frontNormal = Vector3(-1, 0, 0)
        wall9.commit()

        wall10 = Wall()
        wall10.startPoint = Vector3(2, 7, 0)
        wall10.endPoint = Vector3(3, 7, 0)
        wall10.orientation = Orientation.horizontal
        wall10.frontNormal = Vector3(0, 1, 0)
        wall10.commit()

        wall11 = Wall()
        wall11.startPoint = Vector3(3, 6, 0)
        wall11.endPoint = Vector3(3, 7, 0)
        wall11.orientation = Orientation.vertical
        wall11.frontNormal = Vector3(1, 0, 0)
        wall11.commit()

        wall12 = Wall()
        wall12.startPoint = Vector3(2, 6, 0)
        wall12.endPoint = Vector3(3, 6, 0)
        wall12.orientation = Orientation.horizontal
        wall12.frontNormal = Vector3(0, -1, 0)
        wall12.commit()
        # pole

        wall13 = Wall()
        wall13.startPoint = Vector3(0, 7, 0)
        wall13.endPoint = Vector3(3, 10, 0)
        wall13.orientation = Orientation.diagonal
        wall13.frontNormal = Vector3(1, -1, 0)
        wall13.frontNormal.normalize()
        wall13.commit()

        wall14 = Wall()
        wall14.startPoint = Vector3(27, 5, 0)
        wall14.endPoint = Vector3(30, 8, 0)
        wall14.orientation = Orientation.diagonal
        wall14.frontNormal = Vector3(-1, 1, 0)
        wall14.frontNormal.normalize()
        wall14.commit()

        floor1 = FlatFloor()
        floor1.downLeft = Vector3(0, 0, 0)
        floor1.downRight = Vector3(10, 0, 0)
        floor1.upLeft = Vector3(0, 10, 0)
        floor1.upRight = Vector3(10, 10, 0)
        floor1.leftFrontNormal = Vector3(1, 0, 0)
        floor1.rightFrontNormal = Vector3(-1, 0, 0)
        floor1.upFrontNormal = Vector3(0, -1, 0)
        floor1.downFrontNormal = Vector3(0, 1, 0)
        floor1.z = 0

        floor2 = FlatFloor()
        floor2.downLeft = Vector3(10, 5, 0)
        floor2.downRight = Vector3(15, 5, 0)
        floor2.upLeft = Vector3(10, 10, 0)
        floor2.upRight = Vector3(15, 10, 0)
        floor2.leftFrontNormal = Vector3(1, 0, 0)
        floor2.rightFrontNormal = Vector3(-1, 0, 0)
        floor2.upFrontNormal = Vector3(0, -1, 0)
        floor2.downFrontNormal = Vector3(0, 1, 0)
        floor2.z = 0

        floor3 = FlatFloor()
        floor3.downLeft = Vector3(15, 5, 0)
        floor3.downRight = Vector3(20, 5, 0)
        floor3.upLeft = Vector3(15, 10, 0)
        floor3.upRight = Vector3(20, 10, 0)
        floor3.leftFrontNormal = Vector3(1, 0, 0)
        floor3.rightFrontNormal = Vector3(-1, 0, 0)
        floor3.upFrontNormal = Vector3(0, -1, 0)
        floor3.downFrontNormal = Vector3(0, 1, 0)
        floor3.z = 0

        floor4 = PlaneFloor()
        floor4.downLeft = Vector3(20, 5, 0)
        floor4.downRight = Vector3(30, 5, 1)
        floor4.upLeft = Vector3(20, 15, 0)
        floor4.upRight = Vector3(30, 15, 1)
        floor4.leftFrontNormal = Vector3(1, 0, 0)
        floor4.rightFrontNormal = Vector3(-1, 0, 0)
        floor4.upFrontNormal = Vector3(0, -1, 0)
        floor4.downFrontNormal = Vector3(0, 1, 0)
        rightDirection = floor4.downLeft.getDirectionTo(floor4.downRight)
        rightDirection.normalize()
        floor4.upNormal = Geometry.rotatePoint(rightDirection, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor4.commit()

        self.playerPosition = Vector3(2, 2, 0)
        self.playerFrontNormal = Vector3(1, 0, 0)

        self.walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14]
        self.floors = [floor1, floor2, floor3, floor4]
