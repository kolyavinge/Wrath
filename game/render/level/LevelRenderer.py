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
        self.modelMatrix = TransformMatrix4()

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
        mainScene.setUniform("modelMatrix", self.modelMatrix)
        mainScene.setUniform("modelViewMatrix", camera.viewMatrix)
        mainScene.setUniform("modelViewProjectionMatrix", mvpMatrix)
        mainScene.setUniform("normalMatrix", camera.viewMatrix.toMatrix3())
        mainScene.setUniform("maxDepth", CommonConstants.maxDepth)

    def renderLevelSegments(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            self.setLightUniforms(levelSegment)
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                self.setMaterialUniforms(item.material)
                item.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(item.vbo)
                item.texture.unbind()

    def setLightUniforms(self, levelSegment):
        mainScene = self.shaderProgramCollection.mainScene
        # lamps
        mainScene.setUniform("lightsCount", len(levelSegment.lights))
        lightIndex = 0
        for light in levelSegment.lights:
            mainScene.setUniform(f"light[{lightIndex}].color", light.color)
            mainScene.setUniform(f"light[{lightIndex}].position", light.position)
            lightIndex += 1
        # player torch
        torch = self.gameData.playerItems.torch
        if torch.isActive:
            player = self.gameData.player
            mainScene.setUniform("spotsCount", 1)
            mainScene.setUniform("spot[0].color", torch.color)
            mainScene.setUniform("spot[0].position", player.eyePosition)
            mainScene.setUniform("spot[0].direction", player.lookDirection)
            mainScene.setUniform("spot[0].attenuation", torch.attenuation)
            mainScene.setUniform("spot[0].cutoffCos", torch.cutoffCos)
        else:
            mainScene.setUniform("spotsCount", 0)

    def setMaterialUniforms(self, material):
        mainScene = self.shaderProgramCollection.mainScene
        mainScene.setUniform("material.ambient", material.ambient)
        mainScene.setUniform("material.diffuse", material.diffuse)
        mainScene.setUniform("material.specular", material.specular)
        mainScene.setUniform("material.shininess", material.shininess)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
    )
