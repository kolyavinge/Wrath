from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.level.LevelItemRenderCollection import *


class LevelItemRenderer:

    def __init__(
        self,
        renderCollection: LevelItemRenderCollection,
        model3dRenderer: Model3dRenderer,
    ):
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def render(self, shader, levelSegment):
        shader.setModelMatrix(TransformMatrix4.identity)
        model = self.renderCollection.getRenderModel3d(levelSegment)
        self.model3dRenderer.render(model, shader)
