from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.lib.List import List


class Level:

    def __init__(self):
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.lights = []
        self.joinLines = []
        self.powerupAreas = []

    def addWall(self, wall):
        wall.commit()
        self.walls.append(wall)

    def addFloor(self, floor):
        floor.commit()
        self.floors.append(floor)

    def addCeiling(self, ceiling):
        ceiling.commit()
        self.ceilings.append(ceiling)

    def addLight(self, light):
        self.lights.append(light)

    def addJoinLine(self, joinLine):
        joinLine.commit()
        self.joinLines.append(joinLine)

    def addPowerupArea(self, powerupArea):
        self.powerupAreas.append(powerupArea)

    def validate(self):
        allItems = self.walls + self.floors + self.ceilings
        allBorderPoints = List.flatten([item.getBorderPoints() for item in allItems])
        for p in allBorderPoints:
            assert p.x >= 0
            assert p.y >= 0
            assert p.z >= 0
            assert p.x <= CommonConstants.maxLevelSize
            assert p.y <= CommonConstants.maxLevelSize
            assert p.z <= CommonConstants.maxLevelSize

        for w in self.walls:
            w.validate()
