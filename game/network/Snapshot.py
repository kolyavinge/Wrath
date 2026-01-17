class SnapshotDiff:

    # пустой обьект. поля добавляются динамически при создании

    def isEmpty(self):
        return len(self.__dict__) == 0


class Snapshot:

    lastId = 0

    def __init__(self):
        self.id = Snapshot.lastId
        Snapshot.lastId += 1
        self.acknowledged = False

        # остальные поля добавляются динамически при создании


Snapshot.empty = Snapshot()
