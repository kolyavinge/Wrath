class Set:

    @staticmethod
    def getAddedItems(oldSet, newSet):
        return [newValue for newValue in newSet if newValue not in oldSet]

    @staticmethod
    def getRemovedItems(oldSet, newSet):
        return [oldValue for oldValue in oldSet if oldValue not in newSet]
