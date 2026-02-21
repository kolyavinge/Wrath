class Dictionary:

    @staticmethod
    def groupby(array, groupFunc):
        groups = {}
        for item in array:
            key = groupFunc(item)
            if key not in groups:
                groups[key] = [item]
            else:
                groups[key].append(item)

        return groups

    @staticmethod
    def getAddedItems(oldDict, newDict):
        return [newValue for newKey, newValue in newDict.items() if newKey not in oldDict]

    def getAddedItemsWithFilter(oldDict, newDict, filter):
        return [newValue for newKey, newValue in newDict.items() if newKey not in oldDict and filter(newKey, newValue)]

    @staticmethod
    def getRemovedItems(oldDict, newDict):
        return [oldValue for oldKey, oldValue in oldDict.items() if oldKey not in newDict]

    @staticmethod
    def getRemovedItemsWithFilter(oldDict, newDict, filter):
        return [oldValue for oldKey, oldValue in oldDict.items() if oldKey not in newDict and filter(oldKey, oldValue)]
