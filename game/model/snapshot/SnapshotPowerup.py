from game.calc.Vector3 import Vector3


class SnapshotPowerup:

    def __init__(self, id=0, kind=0, position=Vector3()):
        self.id = id
        self.kind = kind
        self.position = position

    def __eq__(self, value):
        return self.id == value.id and self.kind == value.kind and self.position == value.position

    def __hash__(self):
        return hash((self.id.__hash__(), self.kind.__hash__(), self.position.__hash__()))

