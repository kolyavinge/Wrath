from game.anx.DebugSettings import DebugSettings
from game.anx.PersonIdLogic import PersonIdLogic
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.person.Enemy import Enemy
from game.model.person.EnemyLifeBar import EnemyLifeBar
from game.model.person.PersonInputData import PersonInputData
from game.model.person.PersonItems import PersonItems


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

    def init(self, gameState):
        self.initPlayer(gameState)
        self.initEnemies(gameState)

    def initPlayer(self, gameState):
        gameState.player.id = self.personIdLogic.getPlayerId()
        level = gameState.level
        position, frontNormal, weaponType = level.getPlayerInitInfo()
        gameState.player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(gameState.player, frontNormal)
        gameState.player.commitNextPosition()
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.weaponSelector.initWeaponByType(gameState.playerItems, weaponType)
        self.playerLevelSegmentsUpdater.update(gameState)

    def initEnemies(self, gameState):
        if not DebugSettings.allowEnemies:
            return

        for position, frontNormal, weaponType in gameState.level.getEnemyInitInfo():
            self.initEnemy(gameState, position, frontNormal, weaponType)

        self.personFloorUpdater.updateEnemiesNextFloor(gameState)
        self.personFloorUpdater.commitEnemiesNextFloor(gameState)
        self.enemyLevelSegmentsUpdater.update(gameState)

    def initEnemy(self, gameState, position, frontNormal, weaponType):
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
        gameState.allPersonInputData[enemy] = gameState.enemyInputData[enemy]
        gameState.enemyLifeBars[enemy] = EnemyLifeBar()
        self.weaponSelector.initWeaponByType(personItems, weaponType)
