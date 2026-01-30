from game.model.person.FragStatistic import FragStatistic
from game.model.person.PersonStates import LifeCycle


class FragStatisticUpdater:

    def init(self, gameState):
        gameState.personFragStatistic = {}
        for person in gameState.allPerson:
            gameState.personFragStatistic[person] = FragStatistic(person)

    def update(self, gameState):
        collisionData = gameState.collisionData

        for person, bullet in collisionData.personBullet.items():
            if person.lifeCycle == LifeCycle.dead:
                if bullet.canIncreaseFrags:
                    self.increaseFrags(gameState, bullet.ownerPerson)
                self.increaseDeaths(gameState, person)

        for person, ray in collisionData.personRay.items():
            if person.lifeCycle == LifeCycle.dead:
                self.increaseFrags(gameState, ray.ownerPerson)
                self.increaseDeaths(gameState, person)

        for person, explosion in collisionData.personExplosion.items():
            if person.lifeCycle == LifeCycle.dead:
                if explosion.bullet.ownerPerson != person:
                    self.increaseFrags(gameState, explosion.bullet.ownerPerson)
                self.increaseDeaths(gameState, person)

        for person in collisionData.personFalling:
            if person.lifeCycle == LifeCycle.dead:
                self.increaseDeaths(gameState, person)

    def increaseFrags(self, gameState, person):
        gameState.personFragStatistic[person].frags += 1

    def increaseDeaths(self, gameState, person):
        gameState.personFragStatistic[person].deaths += 1
