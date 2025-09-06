from OpenGL.GL import *

from game.anx.PersonConstants import PersonConstants
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory
from game.gl.vbo.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class EnemyLifeBarRenderer:

    def __init__(
        self,
        gameData: GameData,
        shaderProgramCollection: ShaderProgramCollection,
        vboBuilderFactory: VBOBuilderFactory,
        vboRenderer: VBORenderer,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.vboBuilderFactory = vboBuilderFactory
        self.vboRenderer = vboRenderer
        self.lifeBarColor = ColorVector3(50, 250, 0)
        self.lifeBarColor.normalize()
        self.initQuadVBO()

    def render(self):
        plainColor = self.shaderProgramCollection.plainColor
        plainColor.use()
        plainColor.setViewMatrix(self.gameData.camera.viewMatrix)
        plainColor.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        plainColor.setColor(self.lifeBarColor)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        for lifeBar in self.gameData.enemyLifeBars.values():
            if lifeBar.isVisible:
                plainColor.setModelMatrix(lifeBar.modelMatrix)
                plainColor.setAlphaFactor(lifeBar.alpha)
                self.vboRenderer.render(self.quadVBO)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        plainColor.unuse()

    def initQuadVBO(self):
        x = PersonConstants.xyLengthHalf
        z = PersonConstants.zLength + 0.1
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        vboBuilder.addVertex(Vector3(-x, 0, z))
        vboBuilder.addVertex(Vector3(x, 0, z))
        vboBuilder.addVertex(Vector3(x, 0, z + 0.04))
        vboBuilder.addVertex(Vector3(-x, 0, z + 0.04))
        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)
        self.quadVBO = vboBuilder.build()
