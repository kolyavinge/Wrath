class SnapshotRay:

    def __init__(self, id=0, personId=0):

        self.id = id
        self.personId = personId
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
