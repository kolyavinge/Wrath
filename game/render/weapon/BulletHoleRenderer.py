from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.vbo.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection


class BulletHoleRenderer:

    def __init__(
        self,
        gameData: GameData,
        bulletHoleRenderCollection: BulletHoleRenderCollection,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
    ):
        self.gameData = gameData
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer

    def render(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)

        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setColorFactor(0.5)
        shader.setAlphaFactor(1.0)
        for levelSegment in self.gameData.visibleLevelSegments:
            meshes = self.bulletHoleRenderCollection.getRenderMeshes(levelSegment)
            for mesh in meshes:
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)

        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
