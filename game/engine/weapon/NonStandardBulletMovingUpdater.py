from game.engine.GameState import GameState
from game.engine.weapon.PlasmaBulletMovingLogic import PlasmaBulletMovingLogic
from game.model.weapon.Plasma import PlasmaBullet


class NonStandardBulletMovingUpdater:

    def __init__(
        self,
        gameData: GameState,
        plasmaBulletMovingLogic: PlasmaBulletMovingLogic,
    ):
        self.gameData = gameData
        self.bulletMovingLogic = {}
        self.bulletMovingLogic[PlasmaBullet] = plasmaBulletMovingLogic

    def update(self):
        for bullet in self.gameData.bullets:
            bulletType = type(bullet)
            if bulletType in self.bulletMovingLogic:
                self.bulletMovingLogic[bulletType].apply(bullet)
