class Vector3Utils:

    @staticmethod
    def fromStartToEnd(startPoint, endPoint, stepLength, action):
        stepDirection = startPoint.getDirectionTo(endPoint)
        stepsCount = stepDirection.getLength() / stepLength
        stepDirection.setLength(stepLength)
        point = startPoint.copy()
        n = 0
        while n < stepsCount:
            action(point.copy())
            point.add(stepDirection)
            n += 1
