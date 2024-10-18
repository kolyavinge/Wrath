from game.model.level.Floor import Floor


class PlaneFloor(Floor):

    def __init__(self):
        super().__init__()

    def commit(self):
        super().commit()

    def getZ(self, x, y):
        return self.plane.getZ(x, y)
