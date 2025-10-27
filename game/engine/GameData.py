from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.model.Camera import Camera
from game.model.Dashboard import Dashboard
from game.model.level.BackgroundVisibilityData import BackgroundVisibilityData
from game.model.light.Torch import Torch
from game.model.person.AimState import DefaultAimState
from game.model.person.CollisionData import CollisionData
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player


class GameData:

    def __init__(self):
        self.globalTimeMsec = 0
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
        self.personFragStatistic = {}
        self.bullets = []
        self.bulletTraces = []
        self.explosions = []
        self.powerups = []
        self.bloodStains = []
        self.enemyLifeBars = {}
        self.respawnRequests = []
        self.camera = Camera()
        self.aimState = DefaultAimState()
        self.collisionData = CollisionData()
        self.backgroundVisibility = BackgroundVisibilityData()
        self.dashboard = Dashboard()
        # for debug
        self.isDebug = False
        self.noEnemies = True
        self.enemyFreeze = False

    def updateGlobalTime(self):
        self.globalTimeMsec += CommonConstants.mainTimerMsec
