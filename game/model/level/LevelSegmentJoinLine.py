from game.calc.Vector3 import Vector3


class LevelSegmentJoinLine:
    def __init__(self):
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()

    def commit(self):
        self.middlePoint = self.endPoint.getCopy()
        self.middlePoint.sub(self.startPoint)
        self.middlePoint.div(2)
        self.middlePoint.add(self.startPoint)
