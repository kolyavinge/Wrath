class PowerupCollisionDetector:

    def getCollisionResultOrNone(self, person):
        for powerup in person.currentCenterPointLevelSegment.powerups:
            if person.currentCenterPoint.getLengthTo(powerup.pickupPosition) <= 0.5:
                return powerup

        return None


def makePowerupCollisionDetector(resolver):
    return PowerupCollisionDetector()
