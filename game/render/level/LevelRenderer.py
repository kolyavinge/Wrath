from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelItemGroupCollection import LevelItemGroupCollection


class LevelRenderer:

    def __init__(self, gameData, levelItemGroupCollection, vboRenderer, shaderProgramCollection):
        self.gameData = gameData
        self.levelItemGroupCollection = levelItemGroupCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        # self.modelMatrix = TransformMatrix4()

    def init(self):
        self.levelItemGroupCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())

    def render(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.shaderProgramCollection.mainScene.use()
        self.setCommonUniforms()
        self.renderLevelSegments()
        self.shaderProgramCollection.mainScene.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

    def setCommonUniforms(self):
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        mainScene = self.shaderProgramCollection.mainScene
        # mainScene.setModelMatrix("modelMatrix", self.modelMatrix)
        mainScene.setModelViewMatrix(camera.viewMatrix)
        mainScene.setModelViewProjectionMatrix(mvpMatrix)
        mainScene.setNormalMatrix(camera.viewMatrix.toMatrix3())
        mainScene.setMaxDepth(CommonConstants.maxDepth)

    def renderLevelSegments(self):
        mainScene = self.shaderProgramCollection.mainScene
        torch = self.gameData.playerItems.torch
        player = self.gameData.player
        for levelSegment in self.gameData.visibleLevelSegments:
            mainScene.setLight(levelSegment.lights, player, torch)
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                mainScene.setMaterial(item.material)
                item.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(item.vbo)
                item.texture.unbind()


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
    )
