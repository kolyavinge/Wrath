class SnapshotDiff:

    # пустой обьект. поля добавляются динамически при создании

    def isEmpty(self):
        return len(self.__dict__) == 0
