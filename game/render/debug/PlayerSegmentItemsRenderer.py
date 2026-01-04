from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.engine.GameState import GameState
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelItemRenderCollection import *


class PlayerSegmentItemsRenderer:

    def __init__(
        self,
        gameData: GameState,
        renderCollection: LevelItemRenderCollection,
        model3dRenderer: Model3dRenderer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.shaderProgramCollection = shaderProgramCollection

    def render(self):
        shader = self.shaderProgramCollection.plainColor
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setColor(Vector3(1, 0, 0))
        shader.setAlphaFactor(0.2)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        # self.renderCollisionSegments()
        self.renderVisibilitySegments()

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)

        shader.unuse()

    def renderCollisionSegments(self):
        for levelSegment in self.gameData.player.collisionLevelSegments:
            model = self.renderCollection.getRenderModel3d(levelSegment)
            self.model3dRenderer.renderForShadow(model)

    def renderVisibilitySegments(self):
        model = self.renderCollection.getRenderModel3d(self.gameData.player.visibilityLevelSegment)
        self.model3dRenderer.renderForShadow(model)
