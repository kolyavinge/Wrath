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