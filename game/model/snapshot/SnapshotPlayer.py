class SnapshotPlayer:

    @staticmethod
    def make(id, health):
        person = SnapshotPlayer()
        person.id = id
        person.health = health

        return person

    def __init__(self):
        self.id = 0
        self.health = 0

    def __eq__(self, value):
        return self.id == value.id and self.health == value.health

    def __hash__(self):
        return hash((self.id.__hash__(), self.health.__hash__()))

    def toBytes(self, writer):
        writer.write("iB", self.id, self.health)

    @staticmethod
    def fromBytes(reader):
        person = SnapshotPlayer()
        person.id, person.health = reader.read("iB")

        return person
