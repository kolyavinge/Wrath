from game.anx.DebugSettings import DebugSettings
from game.gl.model3d.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.model.weapon.Launcher import LauncherBullet
from game.model.weapon.Plasma import PlasmaBullet
from game.render.weapon.BulletModel3dFactory import BulletModel3dFactory


class BulletRenderCollection:

    def __init__(
        self,
        bulletModel3dFactory: BulletModel3dFactory,
        renderModel3dLoader: RenderModel3dLoader,
    ):
        self.bulletModel3dFactory = bulletModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.models = {}

    def init(self):
        if DebugSettings.isDebug:
            return

        for vbo in self.models:
            vbo.release()

        self.models = {}
        self.makePlasmaBullet()
        self.makeLauncherBullet()

    def makePlasmaBullet(self):
        model = self.bulletModel3dFactory.makePlasmaBullet()
        self.models[PlasmaBullet] = self.renderModel3dLoader.make(model, Material.plasmaBullet)

    def makeLauncherBullet(self):
        model = self.bulletModel3dFactory.makeLauncherBullet()
        self.models[LauncherBullet] = self.renderModel3dLoader.make(model, Material.launcherBullet)

    def getRenderModel3d(self, bulletType):
        return self.models[bulletType]
