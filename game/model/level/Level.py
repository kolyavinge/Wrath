from game.model.level.BSPTree import BSPTree


class Level:

    def __init__(self):
        self.floors = []
        self.bspTree = BSPTree()

    def validate(self):
        for f in self.floors:
            f.validate()
