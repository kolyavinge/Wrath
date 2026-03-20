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
    def getAddedItems(oldList, newList, keyFunc=None):
        if keyFunc is None:
            oldListSet = set(oldList)
            addedItems = [newValue for newValue in newList if newValue not in oldListSet]
        else:
            oldListSet = set([keyFunc(item) for item in oldList])
            addedItems = [newValue for newValue in newList if keyFunc(newValue) not in oldListSet]

        return addedItems

    @staticmethod
    def getRemovedItems(oldList, newList, keyFunc=None):
        if keyFunc is None:
            newListSet = set(newList)
            removedItems = [oldValue for oldValue in oldList if oldValue not in newListSet]
        else:
            newListDict = set([keyFunc(item) for item in newList])
            removedItems = [oldValue for oldValue in oldList if keyFunc(oldValue) not in newListDict]

        return removedItems
