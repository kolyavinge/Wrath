from game.lib.List import List
from game.model.Orientation import Orientation
from game.model.Visible import Visible


class LevelSegment:

    def __init__(self):
        self.constructions = []
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
        return self.constructions + self.walls + self.floors + self.ceilings + self.lights

    def getAllVisibleItems(self):
        return List.where(lambda item: isinstance(item, Visible), self.getAllItems())

    def commit(self):
        self.horizontalVerticalWalls = [w for w in self.walls if w.orientation == Orientation.horizontal or w.orientation == Orientation.vertical]
        self.diagonalWalls = [w for w in self.walls if w.orientation == Orientation.diagonal]
        self.allConstructions = self.constructions + self.walls + self.floors + self.ceilings
