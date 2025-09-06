from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.model.Camera import Camera
from game.model.light.Torch import Torch
from game.model.person.AimState import DefaultAimState
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player


# TODO переместить в папку model\person
class CollisionData:

    def __init__(self):
        self.personBullet = {}
        self.personPerson = {}
        self.personWalls = {}

    def clear(self):
        self.personBullet.clear()
        self.personPerson.clear()
        self.personWalls.clear()


# TODO переместить в папку model\level
class BackgroundVisibilityData:

    def __init__(self):
        self.vertices = []
        self.texCoords = []
        self.horizontalPointsCount = 0
        self.verticalPointsCount = 0


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
        self.bullets = []
        self.bulletTraces = []
        self.explosions = []
        self.powerups = []
        self.bloodStains = []
        self.enemyLifeBars = {}
        self.camera = Camera()
        self.aimState = DefaultAimState()
        self.collisionData = CollisionData()
        self.backgroundVisibility = BackgroundVisibilityData()
        # for debug
        self.isDebug = False
        self.noEnemies = False
        self.enemyFreeze = False

    def updateGlobalTime(self):
        self.globalTimeMsec += CommonConstants.mainTimerMsec
