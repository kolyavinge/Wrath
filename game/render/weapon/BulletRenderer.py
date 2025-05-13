from OpenGL.GL import *

from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.weapon.BulletRenderCollection import BulletRenderCollection


class BulletRenderer:

    def __init__(
        self,
        renderCollection: BulletRenderCollection,
        model3dRenderer: Model3dRenderer,
    ):
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def render(self, shader, levelSegment):
        for bullet in levelSegment.bullets:
            shader.setModelMatrix(bullet.getModelMatrix())
            model = self.renderCollection.getRenderModel3d(type(bullet))
            self.model3dRenderer.render(model, shader)
