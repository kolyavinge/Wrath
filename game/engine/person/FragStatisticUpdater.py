from game.engine.GameState import GameState
from game.model.person.FragStatistic import FragStatistic
from game.model.person.PersonStates import LifeCycle


class FragStatisticUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def init(self):
        self.gameState.personFragStatistic = {}
        for person in self.gameState.allPerson:
            self.gameState.personFragStatistic[person] = FragStatistic(person)

    def update(self):
        collisionData = self.gameState.collisionData

        for person, bullet in collisionData.personBullet.items():
            if person.lifeCycle == LifeCycle.dead:
                if bullet.ownerPerson is not None:  # if bullet is debris -> ownerPerson is None
                    self.increaseFrags(bullet.ownerPerson)
                self.increaseDeaths(person)

        for person, ray in collisionData.personRay.items():
            if person.lifeCycle == LifeCycle.dead:
                self.increaseFrags(ray.ownerPerson)
                self.increaseDeaths(person)

        for person, explosion in collisionData.personExplosion.items():
            if person.lifeCycle == LifeCycle.dead:
                if explosion.bullet.ownerPerson != person:
                    self.increaseFrags(explosion.bullet.ownerPerson)
                self.increaseDeaths(person)

        for person in collisionData.personFalling:
            if person.lifeCycle == LifeCycle.dead:
                self.increaseDeaths(person)

    def increaseFrags(self, person):
        self.gameState.personFragStatistic[person].frags += 1

    def increaseDeaths(self, person):
        self.gameState.personFragStatistic[person].deaths += 1
