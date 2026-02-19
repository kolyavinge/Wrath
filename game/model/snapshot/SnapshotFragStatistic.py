class SnapshotFragStatistic:

    @staticmethod
    def make(personId, value):
        stat = SnapshotFragStatistic()
        stat.personId = personId
        stat.value = value

        return stat

    def __init__(self):
        self.personId = 0
        self.value = 0

    def __eq__(self, value):
        return self.personId == value.personId and self.value == value.value

    def __hash__(self):
        return hash((self.personId.__hash__(), self.value.__hash__()))

    def toBytes(self, writer):
        writer.write("iB", self.personId, self.value)

    @staticmethod
    def fromBytes(reader):
        stat = SnapshotFragStatistic()
        stat.personId, stat.value = reader.read("iB")

        return stat
