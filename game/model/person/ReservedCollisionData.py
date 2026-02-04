from game.lib.TimeLimitedCollection import TimeLimitedCollection


class ReservedCollisionData:

    def __init__(self):
        timeLimit = 100
        self.personBullet = TimeLimitedCollection(timeLimit)
        self.personRay = TimeLimitedCollection(timeLimit)

    def update(self, collisionData):
        self.reserve(collisionData.personBullet, self.personBullet)
        self.reserve(collisionData.personRay, self.personRay)
        self.personBullet.deleteTimeLimitedItems()
        self.personRay.deleteTimeLimitedItems()

    def reserve(self, sourceDic, reservedCollection):
        for personItemPair in sourceDic.items():
            reservedCollection.append(personItemPair)
