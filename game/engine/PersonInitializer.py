from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic
from game.model.person.Enemy import Enemy
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems


class PersonInitializer:

    def __init__(self, gameData, personTurnLogic):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic

    def init(self):
        self.initPlayer()
        self.initEnemies()

    def initPlayer(self):
        level = self.gameData.level
        self.personTurnLogic.orientByFrontNormal(self.gameData.player, level.playerFrontNormal)
        self.gameData.player.moveNextPositionTo(level.playerPosition)
        self.gameData.player.commitNextPosition()

    def initEnemies(self):
        self.initEnemy(Vector3(16, 13.5, 0))

    def initEnemy(self, position):
        enemy = Enemy()
        self.personTurnLogic.orientByFrontNormal(enemy, Vector3(1, 1, 0).getNormalized())
        enemy.moveNextPositionTo(position)
        enemy.commitNextPosition()
        self.gameData.enemies.append(enemy)
        self.gameData.allPerson.append(enemy)
        self.gameData.enemyItems[enemy] = PersonItems()
        self.gameData.enemyInputData[enemy] = PersonInputData()
        self.gameData.allPersonItems[enemy] = self.gameData.enemyItems[enemy]
        self.gameData.allPersonInputData[enemy] = self.gameData.enemyInputData[enemy]


def makePersonInitializer(resolver):
    return PersonInitializer(resolver.resolve(GameData), resolver.resolve(PersonTurnLogic))
