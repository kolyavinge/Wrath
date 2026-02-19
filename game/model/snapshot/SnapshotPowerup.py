from game.calc.Vector3 import Vector3


class SnapshotPowerup:

    @staticmethod
    def make(id, kind, position):
        pu = SnapshotPowerup()
        pu.id = id
        pu.kind = kind
        pu.position = position

        return pu

    def __init__(self):
        self.id = 0
        self.kind = 0
        self.position = Vector3()

    def __eq__(self, value):
        return self.id == value.id and self.kind == value.kind and self.position == value.position

    def __hash__(self):
        return hash((self.id.__hash__(), self.kind.__hash__(), self.position.__hash__()))

    def toBytes(self, writer):
        # position.z записываем как double (64bit)
        # чтобы на принимающей стороне этот поверап попал в тот же сегмент (collision level segment)
        # иначе он может 'провалиться' сквозь пол

        writer.write("iBffd", self.id, self.kind, self.position.x, self.position.y, self.position.z)

    @staticmethod
    def fromBytes(reader):
        pu = SnapshotPowerup()
        pu.id, pu.kind, pu.position.x, pu.position.y, pu.position.z = reader.read("iBffd")

        return pu
