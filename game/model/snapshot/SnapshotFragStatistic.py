class SnapshotFragStatistic:

    def __init__(self):
        self.personId = 0
        self.value = 0

    def __eq__(self, value):
        return self.personId == value.personId and self.value == value.value

    def __hash__(self):
        return hash((self.personId.__hash__(), self.value.__hash__()))
