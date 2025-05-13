from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
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
        self.initAllPersonPairs()

    def initPlayer(self):
        level = self.gameData.level
        position, frontNormal, weaponType = level.getPlayerInitInfo()
        self.gameData.player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(self.gameData.player, frontNormal)
        self.gameData.player.commitNextPosition()
        self.gameData.playerItems.setWeaponByType(weaponType)

    def initEnemies(self):
        if self.gameData.noEnemies:
            return

        for position, frontNormal, weaponType in self.gameData.level.getEnemyInitInfo():
            self.initEnemy(position, frontNormal, weaponType)

    def initEnemy(self, position, frontNormal, weaponType):
        enemy = Enemy()
        enemy.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(enemy, frontNormal)
        enemy.commitNextPosition()
        self.gameData.enemies.append(enemy)
        self.gameData.allPerson.append(enemy)
        personItems = PersonItems()
        personItems.setWeaponByType(weaponType)
        self.gameData.enemyItems[enemy] = personItems
        self.gameData.enemyInputData[enemy] = PersonInputData()
        self.gameData.allPersonItems[enemy] = self.gameData.enemyItems[enemy]
        self.gameData.allPersonInputData[enemy] = self.gameData.enemyInputData[enemy]

    def initAllPersonPairs(self):
        for i in range(0, len(self.gameData.allPerson) - 1):
            for j in range(i + 1, len(self.gameData.allPerson)):
                person1 = self.gameData.allPerson[i]
                person2 = self.gameData.allPerson[j]
                self.gameData.allPersonPairs.append((person1, person2))


def makePersonInitializer(resolver):
    return PersonInitializer(resolver.resolve(GameData), resolver.resolve(PersonTurnLogic))
