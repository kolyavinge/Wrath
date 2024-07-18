class Vector3Utils:

    @staticmethod
    def fromStartToEnd(startPoint, endPoint, stepLength, action):
        stepDirection = endPoint.getCopy()
        stepDirection.sub(startPoint)
        stepsCount = stepDirection.getLength() / stepLength
        stepDirection.setLength(stepLength)
        point = startPoint.getCopy()
        n = 0
        while n < stepsCount:
            action(point.getCopy())
            point.add(stepDirection)
            n += 1
