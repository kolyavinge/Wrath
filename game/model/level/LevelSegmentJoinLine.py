from game.calc.Vector3 import Vector3


class LevelSegmentJoinLine:

    def __init__(self):
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.frontLevelSegment = None
        self.backLevelSegment = None

    def commit(self):
        self.middlePoint = self.startPoint.getDirectionTo(self.endPoint)
        self.middlePoint.div(2)
        self.middlePoint.add(self.startPoint)
        self.points = []
        Vector3.fromStartToEnd(self.startPoint, self.endPoint, 2.0, lambda point: self.points.append(point))

    def __str__(self):
        return f"{self.startPoint} : {self.endPoint}"
