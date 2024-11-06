class List:

    @staticmethod
    def groupby(array, groupFunc):
        groups = {}
        for item in array:
            key = groupFunc(item)
            if key not in groups:
                groups[key] = [item]
            else:
                groups[key].append(item)

        result = []
        for key in groups:
            result.append((key, groups[key]))

        return result

    @staticmethod
    def flatten(lst):
        result = []
        for x in lst:
            result.extend(x)

        return result

    @staticmethod
    def count(condition, lst):
        result = 0
        for item in lst:
            if condition(item):
                result += 1

        return result
