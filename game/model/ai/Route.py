class Route:

    def __init__(self):
        self.points = []

    def addPoint(self, point):
        self.points.append(point)

    def addPointToStart(self, point):
        self.points.insert(0, point)

    def getCurrentPoint(self):
        return self.points[0]

    def removeCurrentPoint(self):
        self.points.remove(self.getCurrentPoint())

    def hasPoints(self):
        return len(self.points) > 0


class NullRoute:

    def addPoint(self, point):
        raise Exception("Operation is not available.")

    def addPointToStart(self, point):
        raise Exception("Operation is not available.")

    def getCurrentPoint(self):
        raise Exception("Operation is not available.")

    def removeCurrentPoint(self):
        raise Exception("Operation is not available.")

    def hasPoints(self):
        return False


NullRoute.instance = NullRoute()
