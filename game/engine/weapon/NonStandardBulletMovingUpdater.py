from game.engine.GameState import GameState
from game.engine.weapon.PlasmaBulletMovingLogic import PlasmaBulletMovingLogic
from game.model.weapon.Plasma import PlasmaBullet


class NonStandardBulletMovingUpdater:

    def __init__(
        self,
        gameState: GameState,
        plasmaBulletMovingLogic: PlasmaBulletMovingLogic,
    ):
        self.gameState = gameState
        self.bulletMovingLogic = {}
        self.bulletMovingLogic[PlasmaBullet] = plasmaBulletMovingLogic

    def update(self):
        for bullet in self.gameState.bullets:
            bulletType = type(bullet)
            if bulletType in self.bulletMovingLogic:
                self.bulletMovingLogic[bulletType].apply(bullet)
