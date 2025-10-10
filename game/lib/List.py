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
