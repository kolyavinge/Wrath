from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.ai.common.PowerupFinder import PowerupFinder
from game.lib.Random import Random
from game.model.ai.BotState import BotState


class WeaponSearchStateHandler:

    def __init__(
        self,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        powerupFinder: PowerupFinder,
    ):
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.powerupFinder = powerupFinder

    def init(self, gameState, bot):
        if not self.powerupFinder.tryFindNearestWeapon(bot):
            bot.aiData.weaponPowerupDelay.set(Random.getInt(200, 500))

    def process(self, gameState, bot, inputData):
        if bot.aiData.route.hasPoints():
            self.movingLogic.followByRoute(bot)
            inputData.goForward = True

    def getNewStateOrNone(self, gameState, bot, botItems):
        if not bot.aiData.route.hasPoints():
            return BotState.patrolling

        return None
