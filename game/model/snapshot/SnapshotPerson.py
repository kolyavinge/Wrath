from game.calc.Vector3 import Vector3


class SnapshotPerson:

    def __init__(self):
        self.id = 0
        self.centerPoint = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0

    def __eq__(self, value):
        return self.centerPoint == value.centerPoint and self.yawRadians == value.yawRadians and self.pitchRadians == value.pitchRadians

    def __hash__(self):
        return hash((self.centerPoint.__hash__(), self.yawRadians.__hash__(), self.pitchRadians.__hash__()))
