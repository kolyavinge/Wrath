from game.calc.Vector3 import Vector3
from game.levels.builder.CeilingBuilder import CeilingBuilder
from game.levels.builder.WallBuilder import WallBuilder
from game.model.level.Ceiling import Ceiling
from game.model.level.Construction import Construction
from game.model.level.Floor import Floor
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.model.light.Light import Light
from game.model.light.RectLamp import RectLamp
from game.model.light.RoundLamp import RoundLamp


class LevelBuilder:

    def __init__(self, level):
        self.level = level
        self.wallBuilder = WallBuilder(self.level)
        self.ceilingBuilder = CeilingBuilder(self.level)

    def buildWalls(self, startPoint, *wallBuildInfoList):
        self.wallBuilder.buildWalls(startPoint, *wallBuildInfoList)

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

    def buildFloor(self, downLeft, xLength, yLength, material):
        floor = Floor()
        floor.downLeft = downLeft
        floor.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        floor.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        floor.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        floor.frontNormal = floor.downLeft.getDirectionTo(floor.downRight)
        floor.frontNormal.vectorProduct(floor.downLeft.getDirectionTo(floor.upLeft))
        floor.frontNormal.normalize()
        floor.material = material
        self.level.addFloor(floor)

    def buildStair(self, downLeft, xLength, yLength, startBasePoint, endBasePoint, stepsCount, stepWidth, material):
        stair = Stair()
        stair.downLeft = downLeft
        stair.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        stair.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        stair.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        stair.startBasePoint = startBasePoint
        stair.endBasePoint = endBasePoint
        stair.stepsCount = stepsCount
        stair.stepWidth = stepWidth
        stair.material = material
        self.level.addFloor(stair)

    def buildBalcony(self, downLeft, downRight, upLeft, upRight, height, topBottomMaterial, edgeMaterial):
        floor = Floor()
        floor.downLeft = downLeft
        floor.downRight = downRight
        floor.upLeft = upLeft
        floor.upRight = upRight
        floor.material = topBottomMaterial
        floor.visualSize = None
        floor.canCastShadow = True
        self.level.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = downRight.copy()
        ceiling.downRight = downLeft.copy()
        ceiling.upLeft = upRight.copy()
        ceiling.upRight = upLeft.copy()
        ceiling.downLeft.z -= height
        ceiling.downRight.z -= height
        ceiling.upLeft.z -= height
        ceiling.upRight.z -= height
        ceiling.material = topBottomMaterial
        ceiling.visualSize = None
        self.level.addCeiling(ceiling)

        edge = Construction()
        edge.downLeft = ceiling.upLeft
        edge.downRight = ceiling.upRight
        edge.upLeft = floor.upRight
        edge.upRight = floor.upLeft
        edge.frontNormal = downLeft.getDirectionTo(upLeft)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

    def buildCeiling(self, downLeft, xLength, yLength, material, hole=None):
        self.ceilingBuilder.buildCeiling(downLeft, xLength, yLength, material, hole)

    def buildLight(self, position, intensity=1.0, joinGroup=None):
        light = Light()
        light.position = position
        light.color.mul(intensity)
        light.joinGroup = joinGroup
        self.level.addLight(light)

    def buildRoundLamp(self, position, frontNormal, radius, height, material, intensity=1.0, joinGroup=None):
        light = RoundLamp()
        light.position = position
        light.color.mul(intensity)
        light.frontNormal = frontNormal
        light.radius = radius
        light.height = height
        light.material = material
        light.joinGroup = joinGroup
        self.level.addLight(light)

    def buildRectLamp(self, position, frontNormal, height, width, long, longNormal, material, intensity=1.0, joinGroup=None):
        light = RectLamp()
        light.position = position
        light.color.mul(intensity)
        light.frontNormal = frontNormal
        light.height = height
        light.width = width
        light.long = long
        light.longNormal = longNormal
        light.material = material
        light.joinGroup = joinGroup
        self.level.addLight(light)
