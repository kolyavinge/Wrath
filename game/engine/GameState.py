from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.engine.UpdateStatistic import UpdateStatistic
from game.lib.LimitedCollection import LimitedCollection
from game.model.level.BackgroundVisibilityData import BackgroundVisibilityData
from game.model.person.Camera import Camera
from game.model.person.CollisionData import CollisionData
from game.model.person.Dashboard import Dashboard
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player
from game.model.person.ReservedCollisionData import ReservedCollisionData


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
        self.allPersonById = {}
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.allPersonInputData = {}
        self.allPersonInputData[self.player] = self.playerInputData
        self.bullets = []
        self.bulletsById = {}
        self.removedBullets = LimitedCollection(CommonConstants.maxRemovedBulletsCount, lambda bullet: bullet.id)
        self.bulletTraces = []
        self.bulletHolePoints = set()  # TODO ограничить кол-во CommonConstants.maxBulletHoles
        self.rays = []
        self.explosions = []
        self.powerups = []
        self.personFragStatistic = {}
        self.collisionData = CollisionData()
        self.reservedCollisionData = ReservedCollisionData()
        self.updateStatistic = UpdateStatistic()

        self.enemyLifeBars = {}

    def updateGlobalTime(self):
        self.globalTimeMsec += CommonConstants.mainTimerMsec
        self.globalTimeSec = self.globalTimeMsec / 1000.0


class ClientGameState(GameState):

    def __init__(self):
        super().__init__()
        self.bloodStains = []
        self.camera = Camera()
        self.backgroundVisibility = BackgroundVisibilityData()
        self.dashboard = Dashboard()


class ServerGameState(GameState):
    pass
