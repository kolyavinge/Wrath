from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTree import BSPTree
from game.engine.UpdateStatistic import UpdateStatistic
from game.lib.IdList import IdList
from game.lib.LimitedIdList import LimitedIdList
from game.model.level.BackgroundVisibilityData import BackgroundVisibilityData
from game.model.person.Camera import Camera
from game.model.person.CollisionData import CollisionData
from game.model.person.Dashboard import Dashboard
from game.model.person.ReservedCollisionData import ReservedCollisionData


class GameState:

    def __init__(self):
        self.globalTimeMsec = 0
        self.globalTimeSec = 0
        self.level = None
        self.collisionTree = BSPTree()
        self.visibilityTree = BSPTree()
        self.visibleLevelSegments = set()
        self.allPerson = IdList()
        self.allPersonItems = {}
        self.allPersonInputData = {}
        self.bullets = IdList()
        self.removedBullets = LimitedIdList(CommonConstants.maxRemovedBulletsCount)
        self.bulletTraces = []
        self.bulletHolePoints = set()  # TODO ограничить кол-во CommonConstants.maxBulletHoles
        self.rays = IdList()
        self.explosions = []
        self.powerups = []
        self.personFragStatistic = {}
        self.collisionData = CollisionData()
        self.reservedCollisionData = ReservedCollisionData()
        self.updateStatistic = UpdateStatistic()

    def updateGlobalTime(self):
        self.globalTimeMsec += CommonConstants.mainTimerMsec
        self.globalTimeSec = self.globalTimeMsec / 1000.0


class ClientGameState(GameState):

    def __init__(self):
        super().__init__()
        self.player = None
        self.playerItems = None
        self.playerInputData = None
        self.enemies = []
        self.enemyItems = {}
        self.enemyInputData = {}
        self.bloodStains = []
        self.camera = Camera()
        self.backgroundVisibility = BackgroundVisibilityData()
        self.enemyLifeBars = {}
        self.dashboard = Dashboard()


class ServerGameState(GameState):

    def __init__(self):
        super().__init__()
        self.players = []
        self.playersItems = {}
        self.bots = []
        self.botItems = {}
        self.botInputData = {}
