class PersonIdLogic:

    def __init__(self):
        self.lastEnemyId = 9
        self.lastNetPlayerId = 99

    def getPlayerId(self):
        return 1

    def getEnemyId(self):
        self.lastEnemyId += 1
        assert self.lastEnemyId < 100

        return self.lastEnemyId

    def getNetPlayerId(self):
        self.lastNetPlayerId += 1

        return self.lastNetPlayerId
