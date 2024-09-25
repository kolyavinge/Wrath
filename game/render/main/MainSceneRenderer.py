from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelItemGroupCollection import LevelItemGroupCollection


class MainSceneRenderer:

    def __init__(self, gameData, levelItemGroupCollection, vboRenderer, shaderProgramCollection):
        self.gameData = gameData
        self.levelItemGroupCollection = levelItemGroupCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection

    def init(self):
        self.levelItemGroupCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())

    def render(self):
        self.calculateLightComponents()
        self.calculateShadowVolumes()
        self.composeScene()

    def calculateLightComponents(self):
        shader = self.shaderProgramCollection.mainSceneLightComponents
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        shader.use()
        self.setCommonUniforms(shader)
        self.renderLevelSegments(shader)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

    def setCommonUniforms(self, shader):
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        shader.setModelViewMatrix(camera.viewMatrix)
        shader.setModelViewProjectionMatrix(mvpMatrix)
        shader.setNormalMatrix(camera.viewMatrix.toMatrix3())
        shader.setMaxDepth(CommonConstants.maxDepth)

    def renderLevelSegments(self, shader):
        torch = self.gameData.playerItems.torch
        player = self.gameData.player
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, player, torch)
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                shader.setMaterial(item.material)
                item.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(item.vbo)
                item.texture.unbind()

    def calculateShadowVolumes(self):
        pass

    def composeScene(self):
        pass


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
    )
