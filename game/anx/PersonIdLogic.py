from game.anx.CommonConstants import CommonConstants


class PersonIdLogic:

    idStep = 1000

    def __init__(self):
        self.lastNetPlayerId = 2000
        self.lastEnemyId = 10000 * CommonConstants.maxServerPlayers

    def getPlayerId(self):
        return 1000

    def getNetPlayerId(self):
        result = self.lastNetPlayerId
        self.lastNetPlayerId += self.idStep

        return result

    def getEnemyId(self):
        result = self.lastEnemyId
        self.lastEnemyId += self.idStep

        return result
