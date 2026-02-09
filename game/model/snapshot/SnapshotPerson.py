from game.calc.Vector3 import Vector3


class SnapshotPerson:

    def __init__(self, id=0, centerPoint=Vector3(), yawRadians=0, pitchRadians=0, health=0):
        self.id = id
        self.centerPoint = centerPoint
        self.yawRadians = yawRadians
        self.pitchRadians = pitchRadians
        self.health = health

    def __eq__(self, value):
        return (
            self.id == value.id
            and self.centerPoint == value.centerPoint
            and self.yawRadians == value.yawRadians
            and self.pitchRadians == value.pitchRadians
            and self.health == value.health
        )

    def __hash__(self):
        return hash(
            (self.id.__hash__(), self.centerPoint.__hash__(), self.yawRadians.__hash__(), self.pitchRadians.__hash__(), self.health.__hash__())
        )

