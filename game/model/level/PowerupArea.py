class PowerupArea:

    def __init__(self, startPoint, endPoint, radius):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.radius = radius

    def __str__(self):
        return f"({self.startPoint}, {self.endPoint}, {self.radius})"
