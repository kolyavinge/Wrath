from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.BufferIndices import BufferIndices
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class BackgroundRenderer:

    def __init__(
        self,
        gameData: GameData,
        vboUpdaterFactory: VBOUpdaterFactory,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        textureCollection: TextureCollection,
    ):
        self.gameData = gameData
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.textureCollection = textureCollection
        self.vbo = self.makeVBO()
        self.vertices = None

    def render(self):
        self.updateVBOIfNeeded()
        # TODO по хорошему тест глубины тут не нужен, но сейчас из-за постороения теней в MainSceneRenderer приходется его тут включать
        glEnable(GL_DEPTH_TEST)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        self.textureCollection.background1.bind(GL_TEXTURE0)
        self.vboRenderer.render(self.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)

    def updateVBOIfNeeded(self):
        if self.vertices != self.gameData.backgroundVisibility.vertices:
            self.vertices = self.gameData.backgroundVisibility.vertices
            self.vboUpdater.beginUpdate(self.vbo)
            i = 0
            for vertex in self.gameData.backgroundVisibility.vertices:
                self.vboUpdater.setVertex(i, vertex)
                i += 1
            i = 0
            for texCoord in self.gameData.backgroundVisibility.texCoords:
                self.vboUpdater.setTexCoord(i, texCoord.x, texCoord.y)
                i += 1
            self.vboUpdater.endUpdate()

    def makeVBO(self):
        backgroundVisibility = self.gameData.backgroundVisibility
        verticesCount = backgroundVisibility.horizontalPointsCount * backgroundVisibility.verticalPointsCount
        facesCount = 2 * (backgroundVisibility.verticalPointsCount - 1) * (backgroundVisibility.horizontalPointsCount - 1)
        vbo = self.vboUpdater.buildUnfilled(verticesCount, facesCount, [BufferIndices.vertices, BufferIndices.texCoords, BufferIndices.faces])
        self.vboUpdater.beginUpdate(vbo)
        self.makeFaces(backgroundVisibility)
        self.vboUpdater.endUpdate()

        return vbo

    def makeFaces(self, backgroundVisibility):
        for row in range(0, backgroundVisibility.verticalPointsCount - 1):
            vertexIndex = row * backgroundVisibility.horizontalPointsCount
            for _ in range(0, backgroundVisibility.horizontalPointsCount - 1):
                upLeft = vertexIndex
                upRight = upLeft + 1
                downLeft = upLeft + backgroundVisibility.horizontalPointsCount
                downRight = downLeft + 1
                self.vboUpdater.addFace(upLeft, downLeft, downRight)
                self.vboUpdater.addFace(upLeft, downRight, upRight)
                vertexIndex += 1
