class SnapshotFragStatistic:

    def __init__(self, personId=0, value=0):
        self.personId = personId
        self.value = value

    def __eq__(self, value):
        return self.personId == value.personId and self.value == value.value

    def __hash__(self):
        return hash((self.personId.__hash__(), self.value.__hash__()))

