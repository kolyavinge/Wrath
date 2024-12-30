from game.model.light.Light import Light
from game.model.Visible import Visible


class VisibleLight(Light, Visible):

    def __init__(self):
        super().__init__()
