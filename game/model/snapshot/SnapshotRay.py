class SnapshotRay:

    @staticmethod
    def make(id, personId):
        ray = SnapshotRay()
        ray.id = id
        ray.personId = personId

        return ray

    def __init__(self):
        self.id = 0
        self.personId = 0
        # weaponNumber не нужен, пока только одно оружие Plasma

    def __eq__(self, value):
        return self.id == value.id and self.personId == value.personId

    def __hash__(self):
        return hash((self.id.__hash__(), self.personId.__hash__()))

    def toBytes(self, writer):
        writer.write("ii", self.id, self.personId)

    @staticmethod
    def fromBytes(reader):
        ray = SnapshotRay()
        ray.id, ray.personId = reader.read("ii")

        return ray
