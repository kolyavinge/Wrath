from game.model.level.Floor import Floor


class NullFloor(Floor):

    def __init__(self):
        super().__init__()


NullFloor.instance = NullFloor()
