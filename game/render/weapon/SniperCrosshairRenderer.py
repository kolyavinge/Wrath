from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory
from game.gl.vbo.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class SniperCrosshairRenderer:

    def __init__(
        self,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        vboBuilderFactory: VBOBuilderFactory,
        textureCollection: TextureCollection,
    ):
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection
        self.crosshairVBO = self.makeCrosshairQuadVBO()
        self.blackVBO = self.makeBlackQuadVBO()
        self.modelMatrix = TransformMatrix4()
        self.modelMatrix.translate((CommonConstants.screenAspect - 1) / 2, 0, 0)
        self.orthoLeft = TransformMatrix4()
        self.orthoLeft.ortho(0, CommonConstants.screenAspect, 0, 1, 0, 1)
        self.orthoRight = TransformMatrix4()
        self.orthoRight.ortho(CommonConstants.screenAspect, 0, 0, 1, 0, 1)
        self.blackColor = Vector3()

    def render(self):
        self.renderCrosshair()
        self.renderBlackQuads()

    def renderCrosshair(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glDisable(GL_DEPTH_TEST)

        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(self.modelMatrix)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.orthoLeft)
        shader.setAlphaFactor(1.0)
        self.textureCollection.sniperCrosshair.bind(GL_TEXTURE0)
        self.vboRenderer.render(self.crosshairVBO)
        shader.unuse()

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def renderBlackQuads(self):
        shader = self.shaderProgramCollection.plainColor
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setColor(self.blackColor)

        shader.setProjectionMatrix(self.orthoLeft)
        self.vboRenderer.render(self.blackVBO)

        shader.setProjectionMatrix(self.orthoRight)
        self.vboRenderer.render(self.blackVBO)

        shader.unuse()

    def makeCrosshairQuadVBO(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(0, 0, 0))
        vboBuilder.addVertex(Vector3(1, 0, 0))
        vboBuilder.addVertex(Vector3(1, 1, 0))
        vboBuilder.addVertex(Vector3(0, 1, 0))

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(0, 1)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo

    def makeBlackQuadVBO(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(0, 0, 0))
        vboBuilder.addVertex(Vector3(0.4, 0, 0))
        vboBuilder.addVertex(Vector3(0.4, 1, 0))
        vboBuilder.addVertex(Vector3(0, 1, 0))

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo
