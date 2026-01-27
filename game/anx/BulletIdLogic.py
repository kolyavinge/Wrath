class BulletIdLogic:

    def __init__(self):
        self.lastBulletId = 0
        self.maxBulletId = 500

    def getNextBulletId(self, personId):
        if self.lastBulletId > self.maxBulletId:
            self.lastBulletId = 0

        self.lastBulletId += 1

        return personId + self.lastBulletId
