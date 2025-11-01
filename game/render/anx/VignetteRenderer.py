from OpenGL.GL import *

from game.gl.ext import gleGetViewportSize
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class VignetteRenderer:

    def __init__(
        self,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        screenQuadVBO: ScreenQuadVBO,
    ):
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.screenQuadVBO = screenQuadVBO

    def render(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        shader = self.shaderProgramCollection.vignette
        shader.use()
        width, height = gleGetViewportSize()
        shader.setResolution(width, height)
        shader.setRadius(0.4)
        shader.setAlphaFactor(0.8)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
