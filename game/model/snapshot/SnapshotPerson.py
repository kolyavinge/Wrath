from game.calc.Vector3 import Vector3


class SnapshotPerson:

    @staticmethod
    def make(id, centerPoint, yawRadians, pitchRadians, health):
        person = SnapshotPerson()
        person.id = id
        person.centerPoint = centerPoint
        person.yawRadians = yawRadians
        person.pitchRadians = pitchRadians
        person.health = health

        return person

    def __init__(self):
        self.id = 0
        self.centerPoint = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0
        self.health = 0

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

    def toBytes(self, writer):
        writer.write("ifffffB", self.id, self.centerPoint.x, self.centerPoint.y, self.centerPoint.z, self.yawRadians, self.pitchRadians, self.health)

    @staticmethod
    def fromBytes(reader):
        person = SnapshotPerson()
        person.id, person.centerPoint.x, person.centerPoint.y, person.centerPoint.z, person.yawRadians, person.pitchRadians, person.health = (
            reader.read("ifffffB")
        )

        return person
