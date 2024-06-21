from game.model.level.BSPTree import BSPTree


class Floor:

    def __init__(self):
        self.walls = []
        self.bspTree = BSPTree()
        self.height = 5

    def validate(self):
        for w in self.walls:
            w.validate()
