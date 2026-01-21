from game.model.weapon.Plasma import PlasmaBullet
from game.render.weapon.anx.PlasmaShineBulletRenderer import PlasmaShineBulletRenderer


class ShineBulletRenderer:

    def __init__(
        self,
        plasmaShineBulletRenderer: PlasmaShineBulletRenderer,
    ):
        self.renderers = {}
        self.renderers[PlasmaBullet] = plasmaShineBulletRenderer

    def render(self, bullets, player, camera):
        for bullet in bullets:
            if type(bullet) in self.renderers:
                renderer = self.renderers[type(bullet)]
                renderer.renderBullet(bullet, player, camera)
