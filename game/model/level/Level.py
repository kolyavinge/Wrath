from game.model.level.BSPTree import BSPTree


class Level:

    def __init__(self):
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.joinLines = []

    def addWall(self, wall):
        wall.commit()
        self.walls.append(wall)

    def addFloor(self, floor):
        self.floors.append(floor)

    def addCeiling(self, ceiling):
        self.ceilings.append(ceiling)

    def addJoinLine(self, joinLine):
        joinLine.commit()
        self.joinLines.append(joinLine)

    def validate(self):
        for w in self.walls:
            w.validate()
