from game.lib.Query import Query
from game.model.Orientation import Orientation
from game.model.Visible import Visible


class LevelSegment:

    def __init__(self):
        # статичные обьекты
        self.constructions = []
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.lights = []
        self.lightsWithJoined = []
        self.joinLines = []
        # динамичные обьекты
        self.powerups = []
        self.bullets = []
        self.bulletTraces = []
        self.weaponFlashes = []
        self.explosions = []
        self.enemies = []
        self.allPerson = []

    def getAllItems(self):  # TODO придумать название по точнее
        return self.constructions + self.walls + self.floors + self.ceilings + self.lights

    def getAllVisibleItems(self):
        return Query(self.getAllItems()).where(lambda item: isinstance(item, Visible)).result

    def commit(self):
        self.horizontalVerticalWalls = [w for w in self.walls if w.orientation == Orientation.horizontal or w.orientation == Orientation.vertical]
        self.diagonalWalls = [w for w in self.walls if w.orientation == Orientation.diagonal]
        self.allConstructions = self.constructions + self.walls + self.floors + self.ceilings
