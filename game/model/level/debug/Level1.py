from game.calc.Vector3 import Vector3
from game.model.level.Level import Level
from game.model.level.Orientation import Orientation
from game.model.level.PlaneGround import PlaneGround
from game.model.level.Wall import Wall


class Level1(Level):

    def __init__(self):
        super().__init__()

        wall1 = Wall()
        wall1.startPoint = Vector3(0, 0, 0)
        wall1.endPoint = Vector3(0, 10, 0)
        wall1.orientation = Orientation.vertical
        wall1.frontNormal = Vector3(1, 0, 0)

        wall2 = Wall()
        wall2.startPoint = Vector3(0, 10, 0)
        wall2.endPoint = Vector3(20, 10, 0)
        wall2.orientation = Orientation.horizontal
        wall2.frontNormal = Vector3(0, -1, 0)

        wall3 = Wall()
        wall3.startPoint = Vector3(20, 10, 0)
        wall3.endPoint = Vector3(20, 15, 0)
        wall3.orientation = Orientation.vertical
        wall3.frontNormal = Vector3(1, 0, 0)

        wall4 = Wall()
        wall4.startPoint = Vector3(20, 15, 0)
        wall4.endPoint = Vector3(30, 15, 0)
        wall4.orientation = Orientation.horizontal
        wall4.frontNormal = Vector3(0, -1, 0)

        wall5 = Wall()
        wall5.startPoint = Vector3(30, 5, 0)
        wall5.endPoint = Vector3(30, 15, 0)
        wall5.orientation = Orientation.vertical
        wall5.frontNormal = Vector3(-1, 0, 0)

        wall6 = Wall()
        wall6.startPoint = Vector3(10, 5, 0)
        wall6.endPoint = Vector3(30, 5, 0)
        wall6.orientation = Orientation.horizontal
        wall6.frontNormal = Vector3(0, 1, 0)

        wall7 = Wall()
        wall7.startPoint = Vector3(10, 0, 0)
        wall7.endPoint = Vector3(10, 5, 0)
        wall7.orientation = Orientation.vertical
        wall7.frontNormal = Vector3(-1, 0, 0)

        wall8 = Wall()
        wall8.startPoint = Vector3(0, 0, 0)
        wall8.endPoint = Vector3(10, 0, 0)
        wall8.orientation = Orientation.horizontal
        wall8.frontNormal = Vector3(0, 1, 0)

        ground1 = PlaneGround()
        ground1.downLeft = Vector3(0, 0, 0)
        ground1.downRight = Vector3(10, 0, 0)
        ground1.upLeft = Vector3(0, 10, 0)
        ground1.upRight = Vector3(10, 10, 0)
        ground1.leftFrontNormal = Vector3(1, 0, 0)
        ground1.rightFrontNormal = Vector3(-1, 0, 0)
        ground1.upFrontNormal = Vector3(0, -1, 0)
        ground1.downFrontNormal = Vector3(0, 1, 0)
        ground1.z = 0

        ground2 = PlaneGround()
        ground2.downLeft = Vector3(20, 5, 0)
        ground2.downRight = Vector3(30, 5, 0)
        ground2.upLeft = Vector3(20, 15, 0)
        ground2.upRight = Vector3(30, 15, 0)
        ground2.leftFrontNormal = Vector3(1, 0, 0)
        ground2.rightFrontNormal = Vector3(-1, 0, 0)
        ground2.upFrontNormal = Vector3(0, -1, 0)
        ground2.downFrontNormal = Vector3(0, 1, 0)
        ground2.z = 0

        ground3 = PlaneGround()
        ground3.downLeft = Vector3(10, 5, 0)
        ground3.downRight = Vector3(15, 5, 0)
        ground3.upLeft = Vector3(10, 10, 0)
        ground3.upRight = Vector3(15, 10, 0)
        ground3.leftFrontNormal = Vector3(1, 0, 0)
        ground3.rightFrontNormal = Vector3(-1, 0, 0)
        ground3.upFrontNormal = Vector3(0, -1, 0)
        ground3.downFrontNormal = Vector3(0, 1, 0)
        ground3.z = 0

        ground4 = PlaneGround()
        ground4.downLeft = Vector3(15, 5, 0)
        ground4.downRight = Vector3(20, 5, 0)
        ground4.upLeft = Vector3(15, 10, 0)
        ground4.upRight = Vector3(20, 10, 0)
        ground4.leftFrontNormal = Vector3(1, 0, 0)
        ground4.rightFrontNormal = Vector3(-1, 0, 0)
        ground4.upFrontNormal = Vector3(0, -1, 0)
        ground4.downFrontNormal = Vector3(0, 1, 0)
        ground4.z = 0

        self.walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]
        self.grounds = [ground1, ground2, ground3, ground4]
