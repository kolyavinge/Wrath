from game.calc.Vector3 import Vector3
from game.model.level.LevelSegment import LevelSegment


class Ray:

    def __init__(self):
        self.startPosition = Vector3()
        self.currentPosition = Vector3()
        self.direction = Vector3()
        self.startLevelSegment = LevelSegment()
        self.currentLevelSegment = LevelSegment()
        self.visibilityLevelSegment = LevelSegment()
        self.length = 0
        self.maxLength = 0
        self.velocityValue = 0
        self.accelValue = 0
        self.damagePercent = 0
        self.weapon = None
        self.holeInfo = None
        self.ownerPerson = None
        self.damagedObject = None
        self.initTimeSec = 0
