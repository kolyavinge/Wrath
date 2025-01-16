from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTree import BSPTree
from game.lib.Math import Math
from game.model.Camera import Camera
from game.model.light.Torch import Torch
from game.model.person.Enemy import Enemy
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
        self.playerItems = PersonItems()  # TODO: можно удалить со временем, allPersonItems будет достаточно
        self.playerInputData = PersonInputData()  # TODO: удалить, allPersonInputData
        self.enemies = []
        self.enemyItems = {}
        self.enemyInputData = {}
        self.playerTorch = Torch()
        self.playerCollidedWalls = []
        self.bullets = []
        self.bulletTraces = []
        self.powerups = []
        self.camera = Camera()
        self.backgroundVisibility = BackgroundVisibilityData()

        enemy1 = Enemy()
        enemy1.yawRadians = Math.piHalf
        enemy1.moveNextPositionTo(Vector3(16, 13.5, 0))
        enemy1.commitNextPosition()
        self.enemies.append(enemy1)

        enemy2 = Enemy()
        enemy2.yawRadians = Math.piHalf
        enemy2.moveNextPositionTo(Vector3(16, 13.5, 4.2))
        enemy2.commitNextPosition()
        self.enemies.append(enemy2)

        enemy3 = Enemy()
        enemy3.yawRadians = Math.piHalf
        enemy3.moveNextPositionTo(Vector3(16, 3.5, 0))
        enemy3.commitNextPosition()
        self.enemies.append(enemy3)

        self.allPerson = [self.player] + self.enemies
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.allPersonItems[enemy1] = PersonItems()
        self.allPersonItems[enemy2] = PersonItems()
        self.allPersonItems[enemy3] = PersonItems()
        self.allPersonInputData = {}
        self.allPersonInputData[self.player] = self.playerInputData
        self.allPersonInputData[enemy1] = PersonInputData()
        self.allPersonInputData[enemy2] = PersonInputData()
        self.allPersonInputData[enemy3] = PersonInputData()


def makeGameData(resolver):
    return GameData()
