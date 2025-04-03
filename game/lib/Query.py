class Query:

    def __init__(self, lst):
        self.result = lst

    def first(self, condition=None):
        for item in self.result:
            if condition == None or condition(item):
                return item

        raise Exception("Collection has no elements.")

    def firstOrNone(self, condition=None):
        for item in self.result:
            if condition == None or condition(item):
                return item

        return None

    def where(self, condition):
        newResult = []
        for item in self.result:
            if condition(item):
                newResult.append(item)

        self.result = newResult

        return self

    def groupby(self, groupFunc):
        groups = {}
        for item in self.result:
            key = groupFunc(item)
            if key not in groups:
                groups[key] = [item]
            else:
                groups[key].append(item)

        newResult = []
        for key in groups:
            newResult.append((key, groups[key]))

        self.result = newResult

        return self

    def flatten(self):
        newResult = []
        for x in self.result:
            newResult.extend(x)

        self.result = newResult

        return self

    def count(self, condition=None):
        result = 0
        for item in self.result:
            if condition is not None:
                if condition(item):
                    result += 1
            else:
                result += 1

        return result
