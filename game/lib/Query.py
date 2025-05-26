class Query:

    def __init__(self, lst):
        self.result = lst

    def first(self, condition=None):
        if condition is not None:
            for item in self.result:
                if condition(item):
                    return item
        else:
            for item in self.result:
                return item

        raise Exception("Element was not found.")

    def firstOrNone(self, condition=None):
        if condition is not None:
            for item in self.result:
                if condition(item):
                    return item
        else:
            for item in self.result:
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
        if condition is None:
            return len(self.result)

        result = 0
        for item in self.result:
            if condition(item):
                result += 1

        return result

    def any(self, condition=None):
        if condition is None:
            return len(self.result) > 0

        for item in self.result:
            if condition(item):
                return True

        return False

    def min(self, minFunc=None):
        if len(self.result) == 0:
            raise Exception("Collection could not be empty.")

        if minFunc is None:
            currentMinValue = self.result[0]
            for item in self.result:
                if item < currentMinValue:
                    currentMinValue = item

            return currentMinValue
        else:
            currentMinValue = minFunc(self.result[0])
            for item in self.result:
                minValue = minFunc(item)
                if minValue < currentMinValue:
                    currentMinValue = minValue

            return currentMinValue

    def max(self, maxFunc=None):
        if len(self.result) == 0:
            raise Exception("Collection could not be empty.")

        if maxFunc is None:
            currentMaxValue = self.result[0]
            for item in self.result:
                if item > currentMaxValue:
                    currentMaxValue = item

            return currentMaxValue
        else:
            currentMaxValue = maxFunc(self.result[0])
            for item in self.result:
                maxValue = maxFunc(item)
                if maxValue > currentMaxValue:
                    currentMaxValue = maxValue

            return currentMaxValue
