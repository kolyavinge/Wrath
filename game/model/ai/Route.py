class Route:

    def __init__(self):
        self.points = []

    def addPoint(self, point):
        self.points.append(point)

    def getCurrentPoint(self):
        return self.points[0]

    def removeCurrentPoint(self):
        self.points.remove(self.getCurrentPoint())

    def hasPoints(self):
        return len(self.points) > 0
