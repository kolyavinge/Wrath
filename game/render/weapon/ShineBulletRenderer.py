from game.engine.GameState import GameState
from game.model.weapon.Plasma import PlasmaBullet
from game.render.weapon.anx.PlasmaShineBulletRenderer import PlasmaShineBulletRenderer


class ShineBulletRenderer:

    def __init__(
        self,
        gameData: GameState,
        plasmaShineBulletRenderer: PlasmaShineBulletRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[PlasmaBullet] = plasmaShineBulletRenderer

    def render(self):
        for bullet in self.gameData.bullets:
            if type(bullet) in self.renderers:
                renderer = self.renderers[type(bullet)]
                renderer.renderBullet(bullet)
