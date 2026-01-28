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
    def getAddedAndRemovedItems(oldDict, newDict):
        addedItems = [newValue for newKey, newValue in newDict.items() if newKey not in oldDict]
        removedItems = [oldValue for oldKey, oldValue in oldDict.items() if oldKey not in newDict]

        return (addedItems, removedItems)
