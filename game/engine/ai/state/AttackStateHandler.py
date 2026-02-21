from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.model.ai.AIData import BotState


class AttackStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def init(self, gameState, bot):
        pass

    def process(self, gameState, bot, inputData):
        bot.aiData.healthPowerupDelay.decrease()
        bot.aiData.weaponPowerupDelay.decrease()

        self.movingLogic.updateMoveDirection(bot)

        if not bot.aiData.runAwayFromObstacle and bot in gameState.collisionData.personPerson:
            bot.aiData.runAwayFromObstacle = True
            otherEnemy = gameState.collisionData.personPerson[bot]
            if bot.velocityValue > 0 and otherEnemy.velocityValue > 0:
                if not bot.velocityVector.isParallel(otherEnemy.velocityVector, 0.1):
                    self.movingLogic.setOppositeMoveDirection(bot)
            else:
                self.movingLogic.setOppositeMoveDirection(bot)

        self.movingLogic.applyMoveDirectionInputData(bot, inputData)

        self.fireLogic.orientToTargetPerson(bot)
        botItems = gameState.allPersonItems[bot]
        self.fireLogic.applyInputData(bot, botItems, inputData)

    def getNewStateOrNone(self, gameState, bot, botItems):
        if bot.health < bot.aiData.criticalHealth and bot.aiData.healthPowerupDelay.isExpired():
            return BotState.healthSearch

        if not self.fireLogic.targetExists(bot, gameState.allPerson):
            return BotState.patrolling

        if not botItems.hasWeapons() and bot.aiData.weaponPowerupDelay.isExpired():
            return BotState.weaponSearch

        return None
