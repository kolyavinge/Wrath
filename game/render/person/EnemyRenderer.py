from OpenGL.GL import *

from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(self, renderCollection, model3dRenderer):
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def render(self, shader, levelSegment):
        model = self.renderCollection.enemyModel
        for enemy in levelSegment.enemies:
            shader.setModelMatrix(enemy.getModelMatrix())
            self.model3dRenderer.render(model, shader)


def makeEnemyRenderer(resolver):
    return EnemyRenderer(resolver.resolve(EnemyRenderCollection), resolver.resolve(Model3dRenderer))
