from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class SniperCrosshairRenderer:

    def __init__(self, shaderProgramCollection, vboRenderer, vboBuilderFactory, textureCollection):
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection
        self.vbo = self.makeQuadVBO()

    def render(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(TransformMatrix4.identity)
        shader.setAlpha(1.0)
        self.textureCollection.sniperCrosshair.bind(GL_TEXTURE0)
        self.vboRenderer.render(self.vbo)
        shader.unuse()

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def makeQuadVBO(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(-1, -1, 0))
        vboBuilder.addVertex(Vector3(1, -1, 0))
        vboBuilder.addVertex(Vector3(1, 1, 0))
        vboBuilder.addVertex(Vector3(-1, 1, 0))

        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(0, 1)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo


def makeSniperCrosshairRenderer(resolver):
    return SniperCrosshairRenderer(
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(TextureCollection),
    )
