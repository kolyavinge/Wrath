from game.lib.Math import Math
from game.lib.Random import Random


class LevelArea:

    def __init__(self, startPoint, endPoint, radius):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.radius = radius

    def getRandomPoint(self):
        if self.startPoint != self.endPoint:
            point = self.startPoint.getDirectionTo(self.endPoint)
            point.setLength(Random.getFloat(0, point.getLength()))
            point.add(self.startPoint)
        else:
            point = self.startPoint.copy()

        if self.radius != 0:
            radius = Random.getFloat(0, self.radius)
            radians = Random.getFloat(0, Math.piDouble)
            x = radius * Math.cos(radians)
            y = radius * Math.sin(radians)
            point.x += x
            point.y += y

        return point

    def __str__(self):
        return f"({self.startPoint}, {self.endPoint}, {self.radius})"


class PowerupArea(LevelArea):
    pass


class RespawnArea(LevelArea):

    def __init__(self, startPoint, endPoint, radius, frontNormal):
        super().__init__(startPoint, endPoint, radius)
        self.frontNormal = frontNormal
