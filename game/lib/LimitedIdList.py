from game.lib.IdList import IdList


class LimitedIdList(IdList):

    def __init__(self, maxCount):
        self.maxCount = maxCount

    def append(self, item):
        if len(self) == self.maxCount:
            self.remove(self[0])

        super().append(item)
