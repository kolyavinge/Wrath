from game.anx.CommonConstants import CommonConstants


class PersonIdLogic:

    idStep = 1000

    def __init__(self):
        self.lastNetPlayerId = 2000
        self.lastBotId = 10000 * CommonConstants.maxServerPlayers

    def getPlayerId(self):
        return 1000

    def getNetPlayerId(self):
        result = self.lastNetPlayerId
        self.lastNetPlayerId += self.idStep

        return result

    def getBotId(self):
        result = self.lastBotId
        self.lastBotId += self.idStep

        return result
