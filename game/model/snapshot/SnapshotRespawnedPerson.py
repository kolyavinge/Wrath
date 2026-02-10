from game.calc.Vector3 import Vector3


class SnapshotRespawnedPerson:

    def __init__(self, id=0, centerPoint=Vector3()):
        self.id = id
        self.centerPoint = centerPoint

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
