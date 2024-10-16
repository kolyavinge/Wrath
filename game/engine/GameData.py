from game.model.Camera import Camera
from game.model.Player import Player
from game.model.PlayerInputData import PlayerInputData
from game.model.PlayerItems import PlayerItems


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = set()
        self.player = Player()
        self.playerInputData = PlayerInputData()
        self.playerItems = PlayerItems()
        self.playerCollidedWalls = []
        self.bullets = []
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
