from game.calc.Vector3 import Vector3


class LevelSegmentJoinLine:
    def __init__(self):
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.frontLevelSegment = None
        self.backLevelSegment = None

    def commit(self):
        self.middlePoint = self.endPoint.getCopy()
        self.middlePoint.sub(self.startPoint)
        self.middlePoint.div(2)
        self.middlePoint.add(self.startPoint)

        self.points = [self.startPoint]
        stepDirection = self.endPoint.getCopy()
        stepDirection.sub(self.startPoint)
        pointsCount = stepDirection.getLength() / 0.5
        stepDirection.setLength(0.5)
        pointNumber = 0
        while pointNumber < pointsCount:
            point = self.points[-1].getCopy()
            point.add(stepDirection)
            self.points.append(point)
            pointNumber += 1
