from OpenGL.GL import *

from game.gl.vbo.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection


class WeaponFlashRenderer:

    def __init__(
        self,
        renderCollection: WeaponFlashRenderCollection,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
    ):
        self.renderCollection = renderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer

    def render(self, camera, visibleLevelSegments):
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setViewMatrix(camera.viewMatrix)
        shader.setProjectionMatrix(camera.projectionMatrix)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)

        for levelSegment in visibleLevelSegments:
            for flash in levelSegment.weaponFlashes:
                mesh = self.renderCollection.getRenderMesh(flash.weaponType)
                shader.setModelMatrix(flash.getModelMatrix())
                shader.setColorFactor(1.0)
                shader.setAlphaFactor(flash.alpha)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()
