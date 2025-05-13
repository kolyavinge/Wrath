from OpenGL.GL import *

from game.engine.GameData import GameData
from game.model.weapon.Plasma import PlasmaBullet
from game.render.weapon.shine.PlasmaShineBulletRenderer import PlasmaShineBulletRenderer


class ShineBulletRenderer:

    def __init__(
        self,
        gameData: GameData,
        plasmaShineBulletRenderer: PlasmaShineBulletRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[PlasmaBullet] = plasmaShineBulletRenderer

    def render(self):
        glEnable(GL_DEPTH_TEST)
        for bullet in self.gameData.bullets:
            if type(bullet) in self.renderers:
                renderer = self.renderers[type(bullet)]
                renderer.renderBullet(bullet)
        glDisable(GL_DEPTH_TEST)


def makeShineBulletRenderer(resolver):
    return ShineBulletRenderer(
        resolver.resolve(GameData),
        resolver.resolve(PlasmaShineBulletRenderer),
    )
