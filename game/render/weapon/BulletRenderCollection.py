from game.gl.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.model.weapon.Launcher import LauncherBullet
from game.render.weapon.BulletModel3dFactory import BulletModel3dFactory


class BulletRenderCollection:

    def __init__(self, bulletModel3dFactory, renderModel3dLoader):
        self.bulletModel3dFactory = bulletModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.models = {}

    def init(self):
        for vbo in self.models:
            vbo.release()

        self.models = {}
        self.makeLauncherBullet()

    def makeLauncherBullet(self):
        model = self.bulletModel3dFactory.makeRocket()
        self.models[LauncherBullet] = self.renderModel3dLoader.make(model, Material.weapon)

    def getRenderModel3d(self, bulletType):
        return self.models[bulletType]


def makeBulletRenderCollection(resolver):
    return BulletRenderCollection(resolver.resolve(BulletModel3dFactory), resolver.resolve(RenderModel3dLoader))
