from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.Numeric import Numeric
from game.model.weapon.Railgun import Railgun
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class RailgunChargingRenderer:

    def __init__(
        self,
        gameData: GameData,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        vboBuilderFactory: VBOBuilderFactory,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vboBuilderFactory = vboBuilderFactory
        self.rangeColor = ColorVector3(89, 22, 36)
        self.rangeColor.normalize()
        self.initVBOs()

    def renderPlayerWeapon(self, railgun):
        if railgun.chargeDelay.isFull():
            return

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        shader = self.shaderProgramCollection.plainColor
        shader.use()
        shader.setModelMatrix(railgun.getModelMatrix())
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setColor(self.rangeColor)

        chargedRanges = self.getChargedRanges(railgun)
        i = 0
        for chargedRange in chargedRanges:
            if chargedRange == 0:
                break
            shader.setAlphaFactor(0.9 * chargedRange)
            self.vboRenderer.render(self.vbo[i])
            i += 1
        shader.unuse()

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def getChargedRanges(self, railgun):
        chargeFactor = 1.0 - (railgun.chargeDelay.value / railgun.chargeDelay.initValue)
        chargedRanges = [
            Numeric.getFillRangeFactor(chargeFactor, 0.0, 0.25),
            Numeric.getFillRangeFactor(chargeFactor, 0.25, 0.5),
            Numeric.getFillRangeFactor(chargeFactor, 0.5, 0.75),
            Numeric.getFillRangeFactor(chargeFactor, 0.75, 1.0),
        ]

        return chargedRanges

    def initVBOs(self):
        self.vbo = [
            self.makeVBO(Railgun.getChargingDisplayPosition(0)),
            self.makeVBO(Railgun.getChargingDisplayPosition(1)),
            self.makeVBO(Railgun.getChargingDisplayPosition(2)),
            self.makeVBO(Railgun.getChargingDisplayPosition(3)),
        ]

    def makeVBO(self, displayPosition):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        p1, p2, p3, p4 = displayPosition
        vboBuilder.addVertex(p1)
        vboBuilder.addVertex(p2)
        vboBuilder.addVertex(p3)
        vboBuilder.addVertex(p4)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo
