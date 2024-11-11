from game.model.Camera import Camera
from game.model.person.Player import Player
from game.model.person.PlayerInputData import PlayerInputData
from game.model.person.PlayerItems import PlayerItems


class GameData:

    def __init__(self):
        self.level = None
        self.visibleLevelSegments = set()
        self.player = Player()
        self.playerInputData = PlayerInputData()
        self.playerItems = PlayerItems()
        self.playerCollidedWalls = []
        self.bullets = []
        self.powerups = []
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
