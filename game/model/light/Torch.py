from game.model.light.Light import Light


class Torch(Light):

    def __init__(self):
        super().__init__()
        self.attenuation = 0.0
        self.cutoffCos = 0.0
        self.isActive = True

    def switch(self):
        self.isActive = not self.isActive
