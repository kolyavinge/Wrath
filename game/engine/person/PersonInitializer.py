from game.anx.DebugSettings import DebugSettings
from game.anx.PersonIdLogic import PersonIdLogic
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.person.Enemy import Enemy
from game.model.person.EnemyLifeBar import EnemyLifeBar
from game.model.person.FragStatistic import FragStatistic
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.weapon.Pistol import Pistol


class PersonInitializer:

    def __init__(
        self,
        personIdLogic: PersonIdLogic,
        personTurnLogic: PersonTurnLogic,
        personFloorUpdater: PersonFloorUpdater,
        weaponSelector: WeaponSelector,
        playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater,
        enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater,
    ):
        self.personIdLogic = personIdLogic
        self.personTurnLogic = personTurnLogic
        self.personFloorUpdater = personFloorUpdater
        self.weaponSelector = weaponSelector
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.enemyLevelSegmentsUpdater = enemyLevelSegmentsUpdater

    def addPersonToClient(self, gameState, personId):
        enemy = Enemy()
        enemy.id = personId
        enemy.commitNextPosition()
        enemy.hasMoved = True
        enemy.hasTurned = True
        gameState.enemies.append(enemy)
        gameState.allPerson.append(enemy)
        personItems = PersonItems()
        gameState.enemyItems[enemy] = personItems
        gameState.enemyInputData[enemy] = PersonInputData()
        gameState.allPersonItems[enemy] = gameState.enemyItems[enemy]
        gameState.allPersonById[enemy.id] = enemy
        gameState.allPersonInputData[enemy] = gameState.enemyInputData[enemy]
        gameState.personFragStatistic[enemy] = FragStatistic(enemy)
        gameState.enemyLifeBars[enemy] = EnemyLifeBar()
        self.weaponSelector.setWeaponByType(personItems, Pistol)
        self.personFloorUpdater.updateEnemiesNextFloor(gameState)
        self.personFloorUpdater.commitEnemiesNextFloor(gameState)
        self.enemyLevelSegmentsUpdater.update(gameState)

        return enemy

    def initPlayer(self, gameState, position, frontNormal, weaponType):
        gameState.player.id = self.personIdLogic.getPlayerId()
        gameState.allPersonById[gameState.player.id] = gameState.player
        gameState.player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(gameState.player, frontNormal)
        gameState.player.commitNextPosition()
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.weaponSelector.setWeaponByType(gameState.playerItems, weaponType)
        gameState.personFragStatistic[gameState.player] = FragStatistic(gameState.player)
        self.playerLevelSegmentsUpdater.update(gameState)

    def addEnemiesToServer(self, gameState, level):
        if not DebugSettings.allowEnemies:
            return

        for position, frontNormal, weaponType in level.getEnemyInitInfo():
            self.addEnemyToServer(gameState, position, frontNormal, weaponType)

        self.personFloorUpdater.updateEnemiesNextFloor(gameState)
        self.personFloorUpdater.commitEnemiesNextFloor(gameState)
        self.enemyLevelSegmentsUpdater.update(gameState)

    def addEnemyToServer(self, gameState, position, frontNormal, weaponType):
        enemy = Enemy()
        enemy.id = self.personIdLogic.getEnemyId()
        enemy.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(enemy, frontNormal)
        enemy.commitNextPosition()
        gameState.enemies.append(enemy)
        gameState.allPerson.append(enemy)
        personItems = PersonItems()
        gameState.enemyItems[enemy] = personItems
        gameState.enemyInputData[enemy] = PersonInputData()
        gameState.allPersonItems[enemy] = gameState.enemyItems[enemy]
        gameState.allPersonById[enemy.id] = enemy
        gameState.allPersonInputData[enemy] = gameState.enemyInputData[enemy]
        gameState.personFragStatistic[enemy] = FragStatistic(enemy)
        self.weaponSelector.setWeaponByType(personItems, weaponType)
