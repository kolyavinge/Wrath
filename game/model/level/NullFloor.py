from game.model.level.Floor import Floor


class NullFloor(Floor):

    def __init__(self):
        super().__init__()
        self.id = 0

    def getZ(self, x, y):
        raise Exception("NullFloor has no z.")


NullFloor.instance = NullFloor()
