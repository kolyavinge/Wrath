from game.calc.Geometry import Geometry
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
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = downLeft
        wall.endPoint = upLeft
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = height
        wall.material = material
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = downRight
        wall.endPoint = upRight
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = height
        wall.material = material
        self.level.addWall(wall)

        wall = Wall()
        wall.startPoint = upLeft
        wall.endPoint = upRight
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = height
        wall.material = material
        self.level.addWall(wall)

    def buildFlatFloor(self, downLeft, xLength, yLength, material, visualSize=1):
        floor = Floor()
        floor.downLeft = downLeft
        floor.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        floor.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        floor.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        floor.frontNormal = Geometry.getNormalVector(floor.downLeft, floor.downRight, floor.upLeft)
        floor.material = material
        floor.visualSize = visualSize
        self.level.addFloor(floor)

    def buildFloor(self, downLeft, downRight, upLeft, upRight, material):
        floor = Floor()
        floor.downLeft = downLeft
        floor.downRight = downRight
        floor.upLeft = upLeft
        floor.upRight = upRight
        floor.frontNormal = Geometry.getNormalVector(floor.downLeft, floor.downRight, floor.upLeft)
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

    def buildSlab(self, downLeft, downRight, upLeft, upRight, height, topBottomMaterial, edgeMaterial, visualSize=2.0):
        floor = Floor()
        floor.downLeft = downLeft
        floor.downRight = downRight
        floor.upLeft = upLeft
        floor.upRight = upRight
        floor.material = topBottomMaterial
        floor.visualSize = visualSize
        self.level.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = downLeft.copy()
        ceiling.downRight = downRight.copy()
        ceiling.upLeft = upLeft.copy()
        ceiling.upRight = upRight.copy()
        ceiling.downLeft.z -= height
        ceiling.downRight.z -= height
        ceiling.upLeft.z -= height
        ceiling.upRight.z -= height
        ceiling.material = topBottomMaterial
        ceiling.visualSize = visualSize
        self.level.addCeiling(ceiling)

        edge = Construction()
        edge.downLeft = ceiling.downLeft
        edge.downRight = ceiling.downRight
        edge.upLeft = floor.downLeft
        edge.upRight = floor.downRight
        edge.frontNormal = upLeft.getDirectionTo(downLeft)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = ceiling.downRight
        edge.downRight = ceiling.upRight
        edge.upLeft = floor.downRight
        edge.upRight = floor.upRight
        edge.frontNormal = downLeft.getDirectionTo(downRight)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = ceiling.upLeft
        edge.downRight = ceiling.upRight
        edge.upLeft = floor.upLeft
        edge.upRight = floor.upRight
        edge.frontNormal = downLeft.getDirectionTo(downRight)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = ceiling.upLeft
        edge.downRight = ceiling.downLeft
        edge.upLeft = floor.upLeft
        edge.upRight = floor.downLeft
        edge.frontNormal = downRight.getDirectionTo(downLeft)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

    def buildRectSlab(self, downLeft, xLength, yLength, height, topBottomMaterial, edgeMaterial, visualSize=2.0):
        downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        self.buildSlab(downLeft, downRight, upLeft, upRight, height, topBottomMaterial, edgeMaterial, visualSize)

    def buildCeiling(self, downLeft, xLength, yLength, material, hole=None):
        self.ceilingBuilder.buildCeiling(downLeft, xLength, yLength, material, hole)

    def buildLight(self, position, intensity=1.0):
        light = Light()
        light.position = position
        light.color.mul(intensity)
        self.level.addLight(light)

    def buildRoundLamp(self, position, frontNormal, radius, height, material, intensity=1.0):
        light = RoundLamp()
        light.position = position
        light.color.mul(intensity)
        light.frontNormal = frontNormal
        light.radius = radius
        light.height = height
        light.material = material
        self.level.addLight(light)

    def buildRectLamp(self, position, frontNormal, height, width, long, longNormal, material, intensity=1.0):
        light = RectLamp()
        light.position = position
        light.color.mul(intensity)
        light.frontNormal = frontNormal
        light.height = height
        light.width = width
        light.long = long
        light.longNormal = longNormal
        light.material = material
        self.level.addLight(light)
