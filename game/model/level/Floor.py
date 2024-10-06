from game.model.level.Construction import Construction


class Floor(Construction):

    def __init__(self):
        super().__init__()
        self.defaultVisualSize = 5.0
