from game.model.Camera import Camera
from game.model.Player import Player
from game.model.PlayerInputData import PlayerInputData


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = set()
        self.player = Player()
        self.playerInputData = PlayerInputData()
        self.playerCollidedWalls = []
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
