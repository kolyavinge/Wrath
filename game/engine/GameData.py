from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTree import BSPTree
from game.lib.Math import Math
from game.model.Camera import Camera
from game.model.light.Torch import Torch
from game.model.person.Enemy import Enemy
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player
from game.model.person.PlayerInputData import PlayerInputData


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
        self.playerInputData = PlayerInputData()
        self.playerItems = PersonItems()
        self.allPersonItems = {}
        self.allPersonItems[self.player] = self.playerItems
        self.playerTorch = Torch()
        self.playerCollidedWalls = []
        self.enemies = []
        self.bullets = []
        self.bulletTraces = []
        self.powerups = []
        self.camera = Camera()
        self.backgroundVisibility = BackgroundVisibilityData()

        enemy = Enemy()
        enemy.yawRadians = Math.piHalf
        enemy.moveNextPositionTo(Vector3(16, 13.5, 0))
        enemy.commitNextPosition()
        self.enemies.append(enemy)

        enemy = Enemy()
        enemy.yawRadians = Math.piHalf
        enemy.moveNextPositionTo(Vector3(16, 13.5, 4.2))
        enemy.commitNextPosition()
        self.enemies.append(enemy)

        enemy = Enemy()
        enemy.yawRadians = Math.piHalf
        enemy.moveNextPositionTo(Vector3(16, 3.5, 0))
        enemy.commitNextPosition()
        self.enemies.append(enemy)

        self.allPerson = [self.player] + self.enemies


def makeGameData(resolver):
    return GameData()
