from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.model.level.Ceiling import Ceiling
from game.model.level.FlatFloor import FlatFloor
from game.model.level.Wall import Wall
from game.model.light.Lamp import Lamp


class LevelBuilder:

    def __init__(self, level):
        self.level = level

    def buildWalls(self, startPoint, *wallBuildInfoList):
        zFightingDelta = 0

        for info in wallBuildInfoList:
            wall = Wall()
            wall.startPoint = startPoint.copy()
            wall.endPoint = info.position.copy()
            wall.frontNormal = info.frontNormal
            wall.height = info.height
            wall.material = info.material
            self.level.addWall(wall)

            if info.bottomBorder is not None:
                depthDirection = info.frontNormal.copy()
                depthDirection.setLength(info.bottomBorder.depth)

                front = Wall()
                front.startPoint = wall.startPoint.copy()
                front.endPoint = wall.endPoint.copy()
                front.startPoint.add(depthDirection)
                front.endPoint.add(depthDirection)
                front.frontNormal = info.frontNormal
                front.height = info.bottomBorder.height
                front.material = info.bottomBorder.frontMaterial
                self.level.addWall(front)

                top = Ceiling()
                top.downLeft = wall.downLeft.copy()
                top.downRight = wall.downRight.copy()
                top.upLeft = wall.downLeft.copy()
                top.upRight = wall.downRight.copy()
                top.downLeft.z += info.bottomBorder.height + zFightingDelta
                top.downRight.z += info.bottomBorder.height + zFightingDelta
                top.upLeft.z += info.bottomBorder.height + zFightingDelta
                top.upRight.z += info.bottomBorder.height + zFightingDelta
                top.upLeft.add(depthDirection)
                top.upRight.add(depthDirection)
                top.frontNormal = CommonConstants.zAxis
                top.material = info.bottomBorder.topMaterial
                self.level.addConstruction(top)
                zFightingDelta += 0.001

            if info.bottomBorder is not None:
                wall.startPoint.z += info.bottomBorder.height
                wall.endPoint.z += info.bottomBorder.height
                wall.height -= info.bottomBorder.height

            startPoint = info.position

    def buildPillar(self, downLeft, size, height, material):
        downLeft = downLeft
        downRight = Vector3(downLeft.x + size, downLeft.y, downLeft.z)
        upLeft = Vector3(downLeft.x, downLeft.y + size, downLeft.z)
        upRight = Vector3(downLeft.x + size, downLeft.y + size, downLeft.z)

        wall = Wall()
        wall.startPoint = downLeft
        wall.endPoint = downRight
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = height
        wall.material = material
        wall.canCastShadow = True
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = downLeft
        wall.endPoint = upLeft
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = height
        wall.material = material
        wall.canCastShadow = True
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = downRight
        wall.endPoint = upRight
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = height
        wall.material = material
        wall.canCastShadow = True
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = upLeft
        wall.endPoint = upRight
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = height
        wall.material = material
        wall.canCastShadow = True
        self.level.addWall(wall)

    def buildFlatFloor(self, downLeft, xLength, yLength, material):
        floor = FlatFloor()
        floor.downLeft = downLeft
        floor.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        floor.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        floor.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        floor.z = downLeft.z
        floor.material = material
        self.level.addFloor(floor)

    def buildCeiling(self, downLeft, xLength, yLength, material):
        ceiling = Ceiling()
        ceiling.downLeft = downLeft
        ceiling.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        ceiling.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        ceiling.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        ceiling.material = material
        self.level.addCeiling(ceiling)

    def buildLamp(self, position):
        light = Lamp()
        light.position = position
        self.level.addLight(light)
