from game.model.light.Spot import Spot


class Torch(Spot):

    def __init__(self):
        super().__init__()
        self.isActive = True

    def switch(self):
        self.isActive = not self.isActive
