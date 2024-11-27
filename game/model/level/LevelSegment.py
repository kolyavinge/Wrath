from game.model.Orientation import Orientation


class LevelSegment:

    def __init__(self):
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.lights = []
        self.powerups = []
        self.lightsWithJoined = []
        self.joinLines = []
        self.bullets = []
        self.bulletTraces = []
        self.weaponFlashes = []

    def getAllItems(self):
        return self.walls + self.floors + self.ceilings + self.lights

    def commit(self):
        self.horizontalVerticalWalls = [w for w in self.walls if w.orientation == Orientation.horizontal or w.orientation == Orientation.vertical]
        self.diagonalWalls = [w for w in self.walls if w.orientation == Orientation.diagonal]
