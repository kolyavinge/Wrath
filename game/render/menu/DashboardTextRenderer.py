from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.TextRenderer import TextRenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class DashboardTextRenderer:

    def __init__(
        self,
        gameData: GameData,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer

    def setData(self, projectionMatrix, viewportWidth):
        self.projectionMatrix = projectionMatrix
        self.viewportWidth = viewportWidth

    def render(self):
        modelMatrix = TransformMatrix4()
        modelMatrix.scale(0.8, 1.0, 1.0)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(modelMatrix)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.projectionMatrix)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        self.updateTextData()
        shader.unuse()

    def updateTextData(self):
        dashboard = self.gameData.dashboard
        textItems = [
            (dashboard.healthStr, 10, 10),
            (dashboard.vestStr, 200, 10),
            (dashboard.bulletsCountStr, self.viewportWidth + 220, 10),
        ]
        self.textRenderer.render(textItems)
