from game.engine.GameData import GameData
from game.engine.weapon.BulletHoleFactory import BulletHoleFactory
from game.lib.EventManager import EventManager, Events


class BulletHoleLogic:

    def __init__(
        self,
        gameData: GameData,
        bulletHoleFactory: BulletHoleFactory,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.bulletHoleFactory = bulletHoleFactory
        self.eventManager = eventManager

    def makeHole(self, collisionPoint, frontNormal, levelSegment, bulletHoleInfo):
        bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, levelSegment, bulletHoleInfo)
        self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)
