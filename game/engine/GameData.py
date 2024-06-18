from game.model.Camera import Camera
from game.model.Player import Player


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = []
        self.player = Player()
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
