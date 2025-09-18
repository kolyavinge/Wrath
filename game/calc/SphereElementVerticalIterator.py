from game.lib.Numeric import Numeric


class SphereElementVerticalIterator:

    def __init__(self, sphere, levelPointIndex):
        if not Numeric.between(levelPointIndex, 0, (sphere.levelPointsCount / 2) - 1):
            raise Exception(f"levelPointIndex must be between [0;{(sphere.levelPointsCount / 2) - 1}].")

        self.sphere = sphere
        self.levelPointIndex = levelPointIndex
        self.levelNumber = -self.sphere.levelsCount
        self.levelNumberStep = 1
        self.current = None

    def move(self):
        if self.levelNumberStep == -1 and self.levelNumber == -self.sphere.levelsCount - 1:
            return False

        self.current = self.sphere.elements[self.levelNumber][self.levelPointIndex]
        self.levelNumber += self.levelNumberStep
        if self.levelNumber == self.sphere.levelsCount:
            self.levelNumber = self.sphere.levelsCount - 1
            self.levelNumberStep = -1
            self.levelPointIndex += int(self.sphere.levelPointsCount / 2)

        return True
