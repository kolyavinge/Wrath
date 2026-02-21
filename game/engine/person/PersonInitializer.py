from game.anx.CommonConstants import CommonConstants
from game.anx.DebugSettings import DebugSettings
from game.anx.PersonIdLogic import PersonIdLogic
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonLevelSegmentsUpdater import PersonLevelSegmentsUpdater
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.person.Bot import Bot
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
        personLevelSegmentsUpdater: PersonLevelSegmentsUpdater,
    ):
        self.personIdLogic = personIdLogic
        self.personTurnLogic = personTurnLogic
        self.personFloorUpdater = personFloorUpdater
        self.weaponSelector = weaponSelector
        self.personLevelSegmentsUpdater = personLevelSegmentsUpdater

    def addEnemyToClient(self, gameState, personId):
        enemy = Person()
        enemy.id = personId
        gameState.enemies.append(enemy)
        gameState.allPerson.append(enemy)
        personItems = PersonItems()
        gameState.enemyItems[enemy] = personItems
        gameState.enemyInputData[enemy] = PersonInputData()
        gameState.allPersonItems[enemy] = personItems
        gameState.allPersonInputData[enemy] = gameState.enemyInputData[enemy]
        gameState.personFragStatistic[enemy] = FragStatistic(enemy)
        gameState.enemyLifeBars[enemy] = EnemyLifeBar()
        self.weaponSelector.setWeaponByType(personItems, Pistol)

        return enemy

    def addPlayerToServer(self, gameState, personId):
        player = Person()
        player.id = personId
        gameState.players.append(player)
        gameState.allPerson.append(player)
        personItems = PersonItems()
        gameState.playersItems[player] = personItems
        gameState.allPersonItems[player] = personItems
        gameState.personFragStatistic[player] = FragStatistic(player)
        self.weaponSelector.setWeaponByType(personItems, Pistol)

        return player

    def initPlayerForClient(self, gameState, position, frontNormal, weaponType, playerId):
        player = Player()
        player.id = playerId
        player.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(player, frontNormal)
        player.commitNextPosition()
        gameState.player = player
        gameState.allPerson.append(player)
        personItems = PersonItems()
        gameState.playerItems = personItems
        gameState.playerInputData = PersonInputData()
        gameState.allPersonItems[player] = personItems
        gameState.allPersonInputData[player] = gameState.playerInputData
        gameState.personFragStatistic[player] = FragStatistic(player)
        self.weaponSelector.setWeaponByType(personItems, weaponType)
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.personLevelSegmentsUpdater.updateForPlayer(gameState)

    def addBotsToServer(self, gameState, level):
        if not DebugSettings.allowBots:
            return

        botInitInfoList = level.getBotInitInfo()
        if len(botInitInfoList) > CommonConstants.maxBots:
            raise Exception("Max bots has exceeded.")

        for position, frontNormal, weaponType in botInitInfoList:
            self.addBotToServer(gameState, position, frontNormal, weaponType)

        self.personFloorUpdater.updateBotsNextFloor(gameState)
        self.personFloorUpdater.commitBotsNextFloor(gameState)
        self.personLevelSegmentsUpdater.updateForAllPerson(gameState)

    def addBotToServer(self, gameState, position, frontNormal, weaponType):
        bot = Bot()
        bot.id = self.personIdLogic.getBotId()
        bot.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(bot, frontNormal)
        bot.commitNextPosition()
        gameState.bots.append(bot)
        gameState.allPerson.append(bot)
        personItems = PersonItems()
        gameState.botItems[bot] = personItems
        gameState.botInputData[bot] = PersonInputData()
        gameState.allPersonItems[bot] = personItems
        gameState.allPersonInputData[bot] = gameState.botInputData[bot]
        gameState.personFragStatistic[bot] = FragStatistic(bot)
        self.weaponSelector.setWeaponByType(personItems, weaponType)
