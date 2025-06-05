from game.anx.PersonConstants import PersonConstants
from game.engine.cm.PersonCeilingCollisionDetector import PersonCeilingCollisionDetector
from game.engine.GameData import GameData
from game.model.person.PersonZState import PersonZState


class PersonCeilingCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        personCeilingCollisionDetector: PersonCeilingCollisionDetector,
    ):
        self.gameData = gameData
        self.personCeilingCollisionDetector = personCeilingCollisionDetector

    def update(self):
        for person in self.gameData.allPerson:
            if person.zState != PersonZState.jumping:
                continue

            ceiling = self.personCeilingCollisionDetector.getCollidedCeilingOrNone(person)
            if ceiling is not None:
                person.setZ(ceiling.downLeft.z - PersonConstants.zLength)
