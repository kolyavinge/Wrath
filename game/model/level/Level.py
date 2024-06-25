from game.model.level.BSPTree import BSPTree


class Level:

    def __init__(self):
        self.bspTree = BSPTree()
        self.walls = []
        self.grounds = []

    def validate(self):
        for w in self.walls:
            w.validate()
