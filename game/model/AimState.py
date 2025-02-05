from game.lib.Math import Math


class DefaultAimState:

    def __init__(self):
        self.verticalViewDegrees = 45
        self.mouseSensibility = 0.004


class SniperAimState:

    def __init__(self):
        self.verticalViewDegreesMax = 15
        self.verticalViewDegreesMin = 5
        self.degreeStep = 2
        self.verticalViewDegrees = self.verticalViewDegreesMax
        self.mouseSensibility = 0.001

    def zoomIn(self):
        self.verticalViewDegrees = Math.max(self.verticalViewDegrees - self.degreeStep, self.verticalViewDegreesMin)

    def zoomOut(self):
        self.verticalViewDegrees = Math.min(self.verticalViewDegrees + self.degreeStep, self.verticalViewDegreesMax)
