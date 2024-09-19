from game.model.level.Orientation import Orientation


class LevelSegment:

    def __init__(self):
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.lights = []
        self.joinLines = []

    def getAllItems(self):
        return self.walls + self.floors + self.ceilings

    def commit(self):
        self.checkSegmentVisibilityWalls = [w for w in self.walls if w.checkSegmentVisibility]
        self.horizontalVerticalWalls = [w for w in self.walls if w.orientation == Orientation.horizontal or w.orientation == Orientation.vertical]
        self.diagonalWalls = [w for w in self.walls if w.orientation == Orientation.diagonal]
