from OpenGL.GL import *

from game.gl.vbo.VBORenderer import VBORenderer
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(self, renderCollection, vboRenderer):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        model = self.renderCollection.enemyModel
        for enemy in levelSegment.enemies:
            shader.setModelMatrix(enemy.getModelMatrix())
            for mesh in model.meshes:
                shader.setMaterial(mesh.material)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)


def makeEnemyRenderer(resolver):
    return EnemyRenderer(resolver.resolve(EnemyRenderCollection), resolver.resolve(VBORenderer))
