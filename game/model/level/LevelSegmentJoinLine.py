class LevelSegmentJoinLine:

    def __init__(self, startPoint, endPoint, frontNormal):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.frontNormal = frontNormal
        self.frontLevelSegment = None
        self.backLevelSegment = None

    def commit(self):
        self.middlePoint = self.startPoint.getDirectionTo(self.endPoint)
        self.middlePoint.div(2)
        self.middlePoint.add(self.startPoint)
        self.points = [self.middlePoint, self.startPoint, self.endPoint]

    def getJoinedLevelSegment(self, levelSegment):
        return self.backLevelSegment if self.frontLevelSegment == levelSegment else self.frontLevelSegment

    def __str__(self):
        return f"{self.startPoint} : {self.endPoint}"
