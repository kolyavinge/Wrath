from game.calc.Vector3 import Vector3


class SnapshotDebris:

    def __init__(self, id=0, personId=0, position=Vector3(), direction=Vector3()):
        self.id = id
        self.personId = personId
        self.position = position
        self.direction = direction

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
