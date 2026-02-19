from game.calc.Vector3 import Vector3


class SnapshotDebris:

    @staticmethod
    def make(id, personId, position, direction):
        debris = SnapshotDebris()
        debris.id = id
        debris.personId = personId
        debris.position = position
        debris.direction = direction

        return debris

    def __init__(self):
        self.id = 0
        self.personId = 0
        self.position = Vector3()
        self.direction = Vector3()

    def __eq__(self, value):
        return self.id == value.id and self.personId == value.personId and self.position == value.position and self.direction == value.direction

    def __hash__(self):
        return hash(
            (
                self.id.__hash__(),
                self.personId.__hash__(),
                self.position.__hash__(),
                self.direction.__hash__(),
            )
        )

    def toBytes(self, writer):
        writer.write(
            "iiffffff",
            self.id,
            self.personId,
            self.position.x,
            self.position.y,
            self.position.z,
            self.direction.x,
            self.direction.y,
            self.direction.z,
        )

    @staticmethod
    def fromBytes(reader):
        debris = SnapshotDebris()
        (
            debris.id,
            debris.personId,
            debris.position.x,
            debris.position.y,
            debris.position.z,
            debris.direction.x,
            debris.direction.y,
            debris.direction.z,
        ) = reader.read("iiffffff")

        return debris
