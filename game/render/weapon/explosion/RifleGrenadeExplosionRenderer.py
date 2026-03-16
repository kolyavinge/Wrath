from game.render.common.TextureCollection import TextureCollection
from game.render.weapon.explosion.FireExplosionRenderer import FireExplosionRenderer


class RifleGrenadeExplosionRenderer:

    def __init__(
        self,
        textureCollection: TextureCollection,
        fireExplosionRenderer: FireExplosionRenderer,
    ):
        self.textureCollection = textureCollection
        self.fireExplosionRenderer = fireExplosionRenderer

    def renderExplosions(self, explosions, globalTimeSec):
        self.fireExplosionRenderer.renderExplosions(explosions, self.textureCollection.launcherExplosion, globalTimeSec)
