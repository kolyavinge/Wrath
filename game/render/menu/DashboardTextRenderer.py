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

    def setData(self, projectionMatrix, viewportWidth, viewportHeight):
        self.projectionMatrix = projectionMatrix
        self.viewportWidth = viewportWidth
        self.viewportHeight = viewportHeight

    def render(self):
        modelMatrix = TransformMatrix4()
        shader = self.shaderProgramCollection.mesh

        shader.use()

        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.projectionMatrix)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)

        modelMatrix.scale(0.8, 1.0, 1.0)
        shader.setModelMatrix(modelMatrix)
        self.updateMainData()

        modelMatrix.scale(0.4, 0.5, 1.0)
        shader.setModelMatrix(modelMatrix)
        self.updateFragsData()

        shader.unuse()

    def updateMainData(self):
        dashboard = self.gameData.dashboard
        textItems = [
            (dashboard.healthStr, 10, 10),
            (dashboard.vestStr, 200, 10),
            (dashboard.bulletsCountStr, self.viewportWidth + 220, 10),
            (dashboard.bulletsCountStr, self.viewportWidth + 220, 10),
        ]
        self.textRenderer.render(textItems)

    def updateFragsData(self):
        dashboard = self.gameData.dashboard
        textItems = []
        for index, stat in enumerate(dashboard.fragStatisticStr):
            y = 2.0 * self.viewportHeight - 80 - (index * 60)
            name, frags, deaths = stat
            textItems.append((name, 20, y))
            textItems.append((frags, 300, y))
            textItems.append((deaths, 400, y))
        self.textRenderer.render(textItems)
