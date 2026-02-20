from game.anx.CommonConstants import CommonConstants
from game.anx.PersonIdLogic import PersonIdLogic


class BulletIdLogic:

    idStep = 2 * CommonConstants.maxDebrisCount

    def __init__(self):
        self.lastBulletId = self.idStep
        self.maxBulletId = PersonIdLogic.idStep

    def getBulletId(self, personId):
        if self.lastBulletId > self.maxBulletId:
            self.lastBulletId = self.idStep

        result = self.lastBulletId
        self.lastBulletId += self.idStep

        return personId + result

    def getDebrisPieceId(self, bulletId, pieceNumber):
        return bulletId + pieceNumber + 1
