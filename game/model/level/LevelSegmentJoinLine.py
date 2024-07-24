from game.calc.Vector3 import Vector3
from game.calc.Vector3Utils import Vector3Utils


class LevelSegmentJoinLine:
    def __init__(self):
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.frontLevelSegment = None
        self.backLevelSegment = None

    def commit(self):
        self.middlePoint = self.endPoint.getDirectionTo(self.startPoint)
        self.middlePoint.div(2)
        self.middlePoint.add(self.startPoint)
        self.points = []
        Vector3Utils.fromStartToEnd(self.startPoint, self.endPoint, 1.0, lambda point: self.points.append(point))
