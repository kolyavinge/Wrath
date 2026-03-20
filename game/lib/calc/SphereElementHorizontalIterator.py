class SphereElementHorizontalIterator:

    def __init__(self, sphere, levelNumber):
        self.sphere = sphere
        self.levelNumber = levelNumber
        self.levelPointIndex = -1
        self.current = None

    def move(self):
        if self.levelPointIndex == self.sphere.levelPointsCount - 1:
            return False

        self.levelPointIndex += 1
        self.current = self.sphere.elements[self.levelNumber][self.levelPointIndex]

        return True
