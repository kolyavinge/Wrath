from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.AIData import BotState


class PatrollingStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        personTurnLogic: PersonTurnLogic,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.personTurnLogic = personTurnLogic

    def init(self, gameState, bot):
        bot.aiData.patrollingTimeLimit.set(Random.getInt(500, 2000))
        bot.aiData.turnTimeLimit.set(Random.getInt(100, 1000))

    def process(self, gameState, bot, inputData):
        bot.aiData.healthPowerupDelay.decrease()
        bot.aiData.weaponPowerupDelay.decrease()

        if self.movingLogic.isTurnTimeLimited(bot):
            bot.aiData.turnTimeLimit.set(Random.getInt(100, 1000))
            self.personTurnLogic.orientToFrontNormal(bot, Vector3.getRandomNormalVector())

        self.movingLogic.orientToFreeDirection(bot, gameState.collisionTree)
        inputData.goForward = True

    def getNewStateOrNone(self, gameState, bot, botItems):
        if bot.aiData.stateTime > bot.aiData.patrollingTimeLimit.value:
            return BotState.idle

        if bot.health < bot.aiData.criticalHealth and bot.aiData.healthPowerupDelay.isExpired():
            return BotState.healthSearch

        if botItems.hasWeapons():
            otherEnemy = self.fireLogic.getEnemyWithinFireDistanceWhoFiringTo(bot, gameState.collisionData)
            if otherEnemy is not None:
                bot.aiData.targetPerson = otherEnemy
                return BotState.attack

        if botItems.hasWeapons() and self.fireLogic.targetExists(bot, gameState.allPerson):
            return BotState.attack

        if not botItems.hasWeapons() and bot.aiData.weaponPowerupDelay.isExpired():
            return BotState.weaponSearch

        return None
