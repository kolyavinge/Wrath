from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.model.Camera import Camera
from game.model.Dashboard import Dashboard
from game.model.level.BackgroundVisibilityData import BackgroundVisibilityData
from game.model.person.AimState import DefaultAimState
from game.model.person.CollisionData import CollisionData
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player


class GameState:

    def __init__(self):
        self.globalTimeMsec = 0
        self.globalTimeSec = 0
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
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.allPersonInputData = {}
        self.allPersonInputData[self.player] = self.playerInputData
        self.bullets = []
        self.bulletsToRemove = []
        self.bulletTraces = []
        self.bulletHolePoints = set()
        self.rays = []
        self.explosions = []
        self.powerups = []
        self.respawnRequests = []
        self.personFragStatistic = {}
        self.collisionData = CollisionData()
        # for player
        self.bloodStains = []
        self.enemyLifeBars = {}
        self.camera = Camera()
        self.aimState = DefaultAimState()
        self.backgroundVisibility = BackgroundVisibilityData()
        self.dashboard = Dashboard()

    def updateGlobalTime(self):
        self.globalTimeMsec += CommonConstants.mainTimerMsec
        self.globalTimeSec = self.globalTimeMsec / 1000.0
