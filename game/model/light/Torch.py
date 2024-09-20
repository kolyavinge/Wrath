from game.model.light.LightSource import LightSource


class Torch(LightSource):

    def __init__(self):
        super().__init__()
        self.attenuation = 0.0
        self.cutoffRadians = 0.0
