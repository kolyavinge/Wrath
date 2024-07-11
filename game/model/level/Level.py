from game.model.level.BSPTree import BSPTree


class Level:

    def __init__(self):
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.walls = []
        self.floors = []
        self.ceilings = []

    def validate(self):
        for w in self.walls:
            w.validate()
