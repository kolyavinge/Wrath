from game.lib.calc.Vector3 import Vector3


class SnapshotRespawnedPerson:

    @staticmethod
    def make(id, centerPoint, frontNormal):
        person = SnapshotRespawnedPerson()
        person.id = id
        person.centerPoint = centerPoint
        person.frontNormal = frontNormal

        return person

    def __init__(self):
        self.id = 0
        self.centerPoint = Vector3()
        self.frontNormal = Vector3()

    def __eq__(self, value):
        return self.id == value.id and self.centerPoint == value.centerPoint and self.frontNormal == value.frontNormal

    def __hash__(self):
        return hash((self.id.__hash__(), self.centerPoint.__hash__(), self.frontNormal.__hash__()))

    def toBytes(self, writer):
        # centerPoint.z передаем как double 64bit, чтобы избежать 'проваливания' персонажа сквозь пол
        writer.write(
            "iffdfff", self.id, self.centerPoint.x, self.centerPoint.y, self.centerPoint.z, self.frontNormal.x, self.frontNormal.y, self.frontNormal.z
        )

    @staticmethod
    def fromBytes(reader):
        person = SnapshotRespawnedPerson()
        (
            person.id,
            person.centerPoint.x,
            person.centerPoint.y,
            person.centerPoint.z,
            person.frontNormal.x,
            person.frontNormal.y,
            person.frontNormal.z,
        ) = reader.read("iffdfff")

        return person
