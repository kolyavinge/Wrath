from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager, Events
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.person.PlayerBloodStainRenderCollection import *


class PlayerBloodStainRenderer:

    def __init__(
        self,
        gameData: GameState,
        renderCollection: PlayerBloodStainRenderCollection,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def render(self):
        if len(self.gameData.bloodStains) == 0:
            return

        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.projection)
        shader.setColorFactor(1.0)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        for bloodStain in self.gameData.bloodStains:
            model = bloodStain.getModelMatrix(self.viewportWidth, self.viewportHeight)
            shader.setModelMatrix(model)
            shader.setAlphaFactor(bloodStain.brightness)
            mesh = self.renderCollection.getRenderMesh(bloodStain.number)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.projection = TransformMatrix4()
        self.projection.ortho(0, self.viewportWidth, 0, self.viewportHeight, -1, 1)
