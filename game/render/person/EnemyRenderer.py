from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(self, gameData, renderCollection, vboRenderer):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        model = self.renderCollection.enemyModel
        # for enemy in levelSegment.enemies:
        for enemy in self.gameData.enemies:
            shader.setModelMatrix(enemy.getModelMatrix())
            for mesh in model.meshes:
                shader.setMaterial(mesh.material)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)


def makeEnemyRenderer(resolver):
    return EnemyRenderer(resolver.resolve(GameData), resolver.resolve(EnemyRenderCollection), resolver.resolve(VBORenderer))
