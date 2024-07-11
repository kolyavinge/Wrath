class LevelSegment:

    def __init__(self):
        self.walls = []
        self.floors = []
        self.ceilings = []

    def isEmpty(self):
        return not self.walls and not self.floors and not self.ceilings
