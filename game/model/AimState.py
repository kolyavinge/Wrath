from game.lib.Math import Math


class DefaultAimState:

    def __init__(self):
        self.verticalViewDegrees = 45


class SniperAimState:

    def __init__(self):
        self.verticalViewDegreesMin = 15
        self.verticalViewDegreesMax = 25
        self.degreesStep = 1
        self.verticalViewDegrees = self.verticalViewDegreesMax

    def zoomIn(self):
        self.verticalViewDegrees = Math.max(self.verticalViewDegrees - self.degreesStep, self.verticalViewDegreesMin)

    def zoomOut(self):
        self.verticalViewDegrees = Math.min(self.verticalViewDegrees + self.degreesStep, self.verticalViewDegreesMax)
