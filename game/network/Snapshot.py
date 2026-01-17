class SnapshotDiff:

    # пустой обьект. поля добавляются динамически при создании

    def isEmpty(self):
        return len(self.__dict__) == 0


class Snapshot:

    def __init__(self, id):
        self.id = id
        self.acknowledged = False
        # остальные поля добавляются динамически при создании


Snapshot.empty = Snapshot(0)
