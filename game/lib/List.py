class List:

    @staticmethod
    def equals(list1, list2):
        return len(list1) == len(list2) and set(list1).issubset(list2)

    @staticmethod
    def isSorted(lst, getFieldFunc):
        iterator = iter(lst)
        prev = getFieldFunc(next(iterator))
        for item in iterator:
            current = getFieldFunc(item)
            if prev <= current:
                prev = current
            else:
                return False

        return True

    @staticmethod
    def removeItemsBetween(lst, startIndex, endIndex):
        for _ in range(startIndex + 1, endIndex):
            lst.remove(lst[startIndex + 1])

    @staticmethod
    def getAddedAndRemovedItems(oldList, newList, keyFunc=None):
        if keyFunc is None:
            oldListSet = set(oldList)
            newListSet = set(newList)
            addedItems = [newValue for newValue in newListSet if newValue not in oldListSet]
            removedItems = [oldValue for oldValue in oldListSet if oldValue not in newListSet]
        else:
            oldListDict = {keyFunc(item): item for item in oldList}
            newListDict = {keyFunc(item): item for item in newList}
            addedItems = [newValue for newKey, newValue in newListDict if newKey not in oldListDict]
            removedItems = [oldValue for oldKey, oldValue in oldListDict if oldKey not in newListDict]

        return (addedItems, removedItems)
