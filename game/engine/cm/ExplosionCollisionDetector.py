from game.model.person.PersonStates import LifeCycle


class ExplosionCollisionDetector:

    def getCollisionResult(self, explosion):
        return [
            person
            for person in explosion.collisionLevelSegment.allPerson
            if person.lifeCycle == LifeCycle.alive and explosion.position.getLengthTo(person.currentCenterPoint) <= explosion.radius
        ]
