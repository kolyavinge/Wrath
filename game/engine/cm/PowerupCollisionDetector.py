class PowerupCollisionDetector:

    def getCollisionResultOrNone(self, person):
        for levelSegment in person.collisionLevelSegments:
            for powerup in levelSegment.powerups:
                if person.currentCenterPoint.getLengthTo(powerup.pickupPosition) <= 0.5:
                    return powerup

        return None


def makePowerupCollisionDetector(resolver):
    return PowerupCollisionDetector()
