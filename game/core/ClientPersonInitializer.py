from game.engine.person.PersonInitializer import PersonInitializer
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.vox.common.VoxManager import VoxManager


class ClientPersonInitializer:

    def __init__(
        self,
        personInitializer: PersonInitializer,
        enemyAnimationCollection: EnemyAnimationCollection,
        voxManager: VoxManager,
    ):
        self.personInitializer = personInitializer
        self.enemyAnimationCollection = enemyAnimationCollection
        self.voxManager = voxManager

    def addPerson(self, gameState, personId):
        person = self.personInitializer.addPersonToClient(gameState, personId)
        self.enemyAnimationCollection.addPerson(person)
        self.voxManager.addPerson(person)
