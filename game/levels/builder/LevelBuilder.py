from game.calc.Vector3 import Vector3
from game.levels.builder.CeilingBuilder import CeilingBuilder
from game.levels.builder.WallBuilder import WallBuilder
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

    def buildCeiling(self, downLeft, xLength, yLength, material, hole=None):
        self.ceilingBuilder.buildCeiling(downLeft, xLength, yLength, material, hole)

    def buildLight(self, position):
        light = Light()
        light.position = position
        self.level.addLight(light)

    def buildRoundLamp(self, position, frontNormal, radius, height, material):
        light = RoundLamp()
        light.position = position
        light.frontNormal = frontNormal
        light.radius = radius
        light.height = height
        light.material = material
        self.level.addLight(light)

    def buildRectLamp(self, position, frontNormal, height, width, long, longNormal, material):
        light = RectLamp()
        light.position = position
        light.frontNormal = frontNormal
        light.height = height
        light.width = width
        light.long = long
        light.longNormal = longNormal
        light.material = material
        self.level.addLight(light)
