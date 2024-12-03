from game.engine.bsp.BSPTree import BSPTree
from game.model.Camera import Camera
from game.model.light.Torch import Torch
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player
from game.model.person.PlayerInputData import PlayerInputData


class GameData:

    def __init__(self):
        self.level = None
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.visibleLevelSegments = set()
        self.player = Player()
        self.playerInputData = PlayerInputData()
        self.playerItems = PersonItems()
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.playerTorch = Torch()
        self.playerCollidedWalls = []
        self.bullets = []
        self.bulletTraces = []
        self.powerups = []
        self.camera = Camera()


def makeGameData(resolver):
    return GameData()
