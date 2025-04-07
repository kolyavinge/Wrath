class List:

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
