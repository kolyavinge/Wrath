from game.calc.Vector3 import Vector3
from game.model.level.LevelSegment import LevelSegment


class Ray:

    def __init__(self):
        self.startPosition = Vector3()
        self.endPosition = Vector3()
        self.startLevelSegment = LevelSegment()
        self.endLevelSegment = LevelSegment()
        self.visibilityLevelSegment = LevelSegment()
        self.damagePercent = 0
        self.weapon = None
        self.ownerPerson = None
        self.damagedObject = None

    def update(self):
        pass
