from game.engine.weapon.PlasmaBulletMovingLogic import PlasmaBulletMovingLogic
from game.model.weapon.Plasma import PlasmaBullet


class NonStandardBulletMovingUpdater:

    def __init__(
        self,
        plasmaBulletMovingLogic: PlasmaBulletMovingLogic,
    ):
        self.bulletMovingLogic = {}
        self.bulletMovingLogic[PlasmaBullet] = plasmaBulletMovingLogic

    def update(self, gameState):
        for bullet in gameState.bullets:
            bulletType = type(bullet)
            if bulletType in self.bulletMovingLogic:
                self.bulletMovingLogic[bulletType].apply(bullet)
