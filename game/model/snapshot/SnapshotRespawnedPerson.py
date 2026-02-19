from game.calc.Vector3 import Vector3


class SnapshotRespawnedPerson:

    @staticmethod
    def make(id, centerPoint):
        person = SnapshotRespawnedPerson()
        person.id = id
        person.centerPoint = centerPoint

        return person

    def __init__(self):
        self.id = 0
        self.centerPoint = Vector3()

    def __eq__(self, value):
        return self.id == value.id and self.centerPoint == value.centerPoint

    def __hash__(self):
        return hash((self.id.__hash__(), self.centerPoint.__hash__()))

    def toBytes(self, writer):
        writer.write("ifff", self.id, self.centerPoint.x, self.centerPoint.y, self.centerPoint.z)

    @staticmethod
    def fromBytes(reader):
        person = SnapshotRespawnedPerson()
        person.id, person.centerPoint.x, person.centerPoint.y, person.centerPoint.z = reader.read("ifff")

        return person
