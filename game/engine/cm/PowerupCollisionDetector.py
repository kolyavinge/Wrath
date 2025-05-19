class PowerupCollisionDetector:

    def getCollisionResultOrNone(self, person):
        for levelSegment in person.collisionLevelSegments:
            for powerup in levelSegment.powerups:
                if person.currentCenterPoint.getLengthTo(powerup.pickupPosition) <= 1.0:
                    return powerup

        return None
