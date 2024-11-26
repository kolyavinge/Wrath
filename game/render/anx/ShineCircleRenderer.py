# https://inspirnathan.com/posts/65-glow-shader-in-shadertoy


from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class ShineCircleParams:

    def __init__(self):
        self.radius = 0
        self.shineColor = Vector3()
        self.shineStrength = 0


class ShineCircleRenderer:

    def __init__(self, gameData, shaderProgramCollection, vboBuilderFactory, vboRenderer):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.vboBuilderFactory = vboBuilderFactory
        self.vboRenderer = vboRenderer
        self.initQuadVBO()

    def render(self, modelMatrix, params):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        circleShader = self.shaderProgramCollection.shineCircle
        circleShader.use()
        circleShader.setModelMatrix(modelMatrix)
        circleShader.setViewMatrix(self.gameData.camera.viewMatrix)
        circleShader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        circleShader.setRadius(params.radius)
        circleShader.setShineColor(params.shineColor)
        circleShader.setShineStrength(params.shineStrength)
        circleShader.setScreenAspect(CommonConstants.screenAspect)
        self.vboRenderer.render(self.quadVBO)
        circleShader.unuse()
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def initQuadVBO(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        side = 1
        vboBuilder.addVertex(Vector3(-side, 0, -side))
        vboBuilder.addVertex(Vector3(side, 0, -side))
        vboBuilder.addVertex(Vector3(side, 0, side))
        vboBuilder.addVertex(Vector3(-side, 0, side))

        vboBuilder.addNormal(Vector3())
        vboBuilder.addNormal(Vector3())
        vboBuilder.addNormal(Vector3())
        vboBuilder.addNormal(Vector3())

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        self.quadVBO = vboBuilder.build()


def makeShineCircleRenderer(resolver):
    return ShineCircleRenderer(
        resolver.resolve(GameData), resolver.resolve(ShaderProgramCollection), resolver.resolve(VBOBuilderFactory), resolver.resolve(VBORenderer)
    )
