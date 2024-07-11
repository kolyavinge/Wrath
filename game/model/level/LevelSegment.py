class LevelSegment:

    def __init__(self):
        self.walls = []
        self.floors = []

    def isEmpty(self):
        return not self.walls and not self.floors

    def validate(self):
        pass
