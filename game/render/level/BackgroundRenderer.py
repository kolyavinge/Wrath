from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.gl.BufferIndices import BufferIndices
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class BackgroundRenderer:

    def __init__(
        self,
        gameState: GameState,
        vboUpdaterFactory: VBOUpdaterFactory,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        textureCollection: TextureCollection,
    ):
        self.gameState = gameState
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.textureCollection = textureCollection
        sphereElementsCountHalf = self.gameState.backgroundVisibility.sphere.elementsCount
        self.vbo = self.vboUpdater.buildUnfilled(
            4 * sphereElementsCountHalf, 2 * sphereElementsCountHalf, [BufferIndices.vertices, BufferIndices.texCoords, BufferIndices.faces]
        )
        self.visibleSphereElements = None

    def render(self):
        self.updateVBOIfNeeded()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameState.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameState.camera.projectionMatrix)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        self.textureCollection.background1.bind(GL_TEXTURE0)
        self.vboRenderer.render(self.vbo)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_DEPTH_TEST)

    def updateVBOIfNeeded(self):
        if self.visibleSphereElements == self.gameState.backgroundVisibility.visibleSphereElements:
            return
        self.visibleSphereElements = self.gameState.backgroundVisibility.visibleSphereElements
        self.vbo.reset()
        for element in self.visibleSphereElements:
            self.vboUpdater.beginUpdate(self.vbo)
            for point in element.points:
                self.vboUpdater.addVertex(point.vertex)
                self.vboUpdater.addTexCoord(point.texCoord.x, point.texCoord.y)
            self.vboUpdater.addFace(0, 1, 2)
            self.vboUpdater.addFace(0, 2, 3)
            self.vboUpdater.endUpdate()
