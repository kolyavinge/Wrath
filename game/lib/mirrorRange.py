def mirrorRange(stepValue, stepsCount):
    for i in range(0, stepsCount + 1):
        yield i * stepValue

    for i in range(1, stepsCount):
        yield (stepsCount - i) * stepValue
