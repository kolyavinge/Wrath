from game.calc.Vector3 import Vector3
from game.levels.builder.CeilingBuilder import CeilingBuilder
from game.levels.builder.WallBuilder import WallBuilder
from game.model.level.Ceiling import Ceiling
from game.model.level.Construction import Construction
from game.model.level.FlatFloor import FlatFloor
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

    def buildFlatFloor(self, downLeft, xLength, yLength, material):
        floor = FlatFloor()
        floor.downLeft = downLeft
        floor.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        floor.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        floor.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        floor.z = downLeft.z
        floor.material = material
        self.level.addFloor(floor)

    def buildBalcony(self, downLeft, downRight, upLeft, upRight, height, topBottomMaterial, edgeMaterial):
        floor = FlatFloor()
        floor.downLeft = downLeft
        floor.downRight = downRight
        floor.upLeft = upLeft
        floor.upRight = upRight
        floor.z = downLeft.z
        floor.material = topBottomMaterial
        floor.canCastShadow = True
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
        ceiling.canCastShadow = True
        self.level.addCeiling(ceiling)

        edge = Construction()
        edge.downLeft = ceiling.upRight
        edge.downRight = ceiling.upLeft
        edge.upLeft = floor.upRight
        edge.upRight = floor.upLeft
        edge.frontNormal = downLeft.getDirectionTo(upLeft)
        edge.frontNormal.normalize()
        edge.material = edgeMaterial
        self.level.addConstruction(edge)

    def buildCeiling(self, downLeft, xLength, yLength, material, hole=None):
        self.ceilingBuilder.buildCeiling(downLeft, xLength, yLength, material, hole)

    def buildLight(self, position, joinGroup=None):
        light = Light()
        light.position = position
        light.joinGroup = joinGroup
        self.level.addLight(light)

    def buildRoundLamp(self, position, frontNormal, radius, height, material, joinGroup=None):
        light = RoundLamp()
        light.position = position
        light.frontNormal = frontNormal
        light.radius = radius
        light.height = height
        light.material = material
        light.joinGroup = joinGroup
        self.level.addLight(light)

    def buildRectLamp(self, position, frontNormal, height, width, long, longNormal, material, joinGroup=None):
        light = RectLamp()
        light.position = position
        light.frontNormal = frontNormal
        light.height = height
        light.width = width
        light.long = long
        light.longNormal = longNormal
        light.material = material
        light.joinGroup = joinGroup
        self.level.addLight(light)
