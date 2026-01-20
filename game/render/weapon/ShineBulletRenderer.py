from game.engine.GameState import GameState
from game.model.weapon.Plasma import PlasmaBullet
from game.render.weapon.anx.PlasmaShineBulletRenderer import PlasmaShineBulletRenderer


class ShineBulletRenderer:

    def __init__(
        self,
        gameState: GameState,
        plasmaShineBulletRenderer: PlasmaShineBulletRenderer,
    ):
        self.gameState = gameState
        self.renderers = {}
        self.renderers[PlasmaBullet] = plasmaShineBulletRenderer

    def render(self):
        for bullet in self.gameState.bullets:
            if type(bullet) in self.renderers:
                renderer = self.renderers[type(bullet)]
                renderer.renderBullet(bullet, self.gameState.player, self.gameState.camera)
