from game.anx.DebugSettings import DebugSettings
from game.engine.GameState import GameState
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.person.Enemy import Enemy
from game.model.person.EnemyLifeBar import EnemyLifeBar
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems


class PersonInitializer:

    def __init__(
        self,
        gameState: GameState,
        personTurnLogic: PersonTurnLogic,
        weaponSelector: WeaponSelector,
    ):
        self.gameState = gameState
        self.personTurnLogic = personTurnLogic
        self.weaponSelector = weaponSelector

    def init(self):
        self.initPlayer()
        self.initEnemies()
        self.initAllPersonPairs()

    def initPlayer(self):
        level = self.gameState.level
        position, frontNormal, weaponType = level.getPlayerInitInfo()
        self.gameState.player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(self.gameState.player, frontNormal)
        self.gameState.player.commitNextPosition()
        self.weaponSelector.initWeaponByType(self.gameState.player, weaponType)

    def initEnemies(self):
        if DebugSettings.noEnemies:
            return

        for position, frontNormal, weaponType in self.gameState.level.getEnemyInitInfo():
            self.initEnemy(position, frontNormal, weaponType)

    def initEnemy(self, position, frontNormal, weaponType):
        enemy = Enemy()
        enemy.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(enemy, frontNormal)
        enemy.commitNextPosition()
        self.gameState.enemies.append(enemy)
        self.gameState.allPerson.append(enemy)
        personItems = PersonItems()
        self.gameState.enemyItems[enemy] = personItems
        self.gameState.enemyInputData[enemy] = PersonInputData()
        self.gameState.allPersonItems[enemy] = self.gameState.enemyItems[enemy]
        self.gameState.allPersonInputData[enemy] = self.gameState.enemyInputData[enemy]
        self.gameState.enemyLifeBars[enemy] = EnemyLifeBar()
        self.weaponSelector.initWeaponByType(enemy, weaponType)

    def initAllPersonPairs(self):
        for i in range(0, len(self.gameState.allPerson) - 1):
            for j in range(i + 1, len(self.gameState.allPerson)):
                person1 = self.gameState.allPerson[i]
                person2 = self.gameState.allPerson[j]
                self.gameState.allPersonPairs.append((person1, person2))
