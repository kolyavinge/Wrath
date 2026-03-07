from game.calc.Vector3 import Vector3


class SnapshotPerson:

    @staticmethod
    def makeWithDefaultValues():
        person = SnapshotPerson()
        person.id = 0
        person.centerPoint = Vector3()
        person.yawRadians = 0
        person.pitchRadians = 0
        person.health = 0
        person.jumpingValue = 0

        return person

    def __init__(self):
        self.id = 0
        self.centerPoint = None
        self.yawRadians = None
        self.pitchRadians = None
        self.health = None
        self.jumpingValue = None
