from game.engine.bsp.BSPTree import BSPTree
from game.model.Camera import Camera
from game.model.light.Torch import Torch
from game.model.person.AimState import DefaultAimState
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player


class BackgroundVisibilityData:

    def __init__(self):
        self.vertices = []
        self.texCoords = []
        self.horizontalPointsCount = 0
        self.verticalPointsCount = 0


class GameData:

    def __init__(self):
        self.level = None
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.visibleLevelSegments = set()
        self.player = Player()
        self.playerItems = PersonItems()
        self.playerInputData = PersonInputData()
        self.enemies = []
        self.enemyItems = {}
        self.enemyInputData = {}
        self.allPerson = [self.player]
        self.allPersonPairs = []
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.allPersonInputData = {}
        self.allPersonInputData[self.player] = self.playerInputData
        self.playerTorch = Torch()
        self.bullets = []
        self.bulletTraces = []
        self.powerups = []
        self.camera = Camera()
        self.aimState = DefaultAimState()
        self.backgroundVisibility = BackgroundVisibilityData()
        self.woundedPerson = {}
        # for debug
        self.isDebug = False
        self.noEnemies = False
