from game.lib.Query import Query
from game.model.level.VisibleLevelItem import VisibleLevelItem
from game.model.Orientation import Orientation


class LevelSegment:

    def __init__(self):
        # статичные обьекты
        self.constructions = []
        self.walls = []
        self.floors = []
        self.ceilings = []
        self.lights = []

        # дополнительные статичные обьекты
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

    def getAllStaticItems(self):
        return self.constructions + self.walls + self.floors + self.ceilings + self.lights

    def getAllVisibleStaticItems(self):
        return Query(self.getAllStaticItems()).where(lambda item: isinstance(item, VisibleLevelItem)).result

    def commit(self):
        self.horizontalVerticalWalls = [w for w in self.walls if w.orientation == Orientation.horizontal or w.orientation == Orientation.vertical]
        self.diagonalWalls = [w for w in self.walls if w.orientation == Orientation.diagonal]
        self.allConstructions = self.constructions + self.walls + self.floors + self.ceilings
