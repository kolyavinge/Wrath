class SnapshotFragStatistic:

    def __init__(self, personId=0, value=0):
        self.personId = personId
        self.value = value

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
