class Vector3Utils:

    @staticmethod
    def fromStartToEnd(startPoint, endPoint, stepLength, action):
        stepDirection = startPoint.getDirectionTo(endPoint)
        stepsCount = int(stepDirection.getLength() / stepLength)
        stepDirection.setLength(stepLength)
        point = startPoint.copy()
        for _ in range(stepsCount):
            action(point.copy())
            point.add(stepDirection)
        action(endPoint.copy())

    @staticmethod
    def splitFromStartToEnd(startPoint, endPoint, stepLength):
        result = []
        Vector3Utils.fromStartToEnd(startPoint, endPoint, stepLength, lambda point: result.append(point))

        return result
