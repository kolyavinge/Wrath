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
from game.model.person.Person import Person
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems
from game.model.person.Player import Player
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
        person = Person()
        person.id = personId
        person.commitNextPosition()
        gameState.enemies.append(person)
        gameState.allPerson.append(person)
        personItems = PersonItems()
        gameState.enemyItems[person] = personItems
        gameState.enemyInputData[person] = PersonInputData()
        gameState.allPersonItems[person] = personItems
        gameState.allPersonById[person.id] = person
        gameState.allPersonInputData[person] = gameState.enemyInputData[person]
        gameState.personFragStatistic[person] = FragStatistic(person)
        gameState.enemyLifeBars[person] = EnemyLifeBar()
        self.weaponSelector.setWeaponByType(personItems, Pistol)

        return person

    def addPlayerToServer(self, gameState, personId):
        person = Person()
        person.id = personId
        person.commitNextPosition()
        gameState.players.append(person)
        gameState.allPerson.append(person)
        personItems = PersonItems()
        gameState.playersItems[person] = personItems
        gameState.allPersonItems[person] = personItems
        gameState.allPersonById[person.id] = person
        gameState.personFragStatistic[person] = FragStatistic(person)
        self.weaponSelector.setWeaponByType(personItems, Pistol)

        return person

    def initPlayer(self, gameState, position, frontNormal, weaponType, playerId=None):
        player = Player()
        player.id = playerId or self.personIdLogic.getPlayerId()
        player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(player, frontNormal)
        player.commitNextPosition()
        gameState.player = player
        gameState.allPerson.append(player)
        personItems = PersonItems()
        gameState.playerItems = personItems
        gameState.playerInputData = PersonInputData()
        gameState.allPersonItems[player] = personItems
        gameState.allPersonById[player.id] = player
        gameState.allPersonInputData[player] = gameState.playerInputData
        gameState.personFragStatistic[player] = FragStatistic(player)
        self.weaponSelector.setWeaponByType(personItems, weaponType)
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.playerLevelSegmentsUpdater.updateForPlayer(gameState)

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
        gameState.allPersonItems[enemy] = personItems
        gameState.allPersonById[enemy.id] = enemy
        gameState.allPersonInputData[enemy] = gameState.enemyInputData[enemy]
        gameState.personFragStatistic[enemy] = FragStatistic(enemy)
        self.weaponSelector.setWeaponByType(personItems, weaponType)
