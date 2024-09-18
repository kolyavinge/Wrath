import numpy
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
        self.modelMatrixFloat32Array = TransformMatrix4().toFloat32Array()

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
        mainScene.setUniform("modelMatrix", self.modelMatrixFloat32Array)
        mainScene.setUniform("modelViewMatrix", camera.viewMatrix.toFloat32Array())
        mainScene.setUniform("modelViewProjectionMatrix", mvpMatrix.toFloat32Array())
        mainScene.setUniform("normalMatrix", camera.viewMatrix.toMatrix3().toFloat32Array())
        mainScene.setUniform("cameraPosition", camera.position.toFloat32Array())
        mainScene.setUniform("maxViewDepth", CommonConstants.maxViewDepthFloat32)

    def renderLevelSegments(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                self.setMaterialUniforms(item.material)
                item.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(item.vbo)
                item.texture.unbind()

    def setMaterialUniforms(self, material):
        mainScene = self.shaderProgramCollection.mainScene
        mainScene.setUniform("material.ambient", numpy.float32(material.ambient))
        mainScene.setUniform("material.diffuse", numpy.float32(material.diffuse))
        mainScene.setUniform("material.specular", numpy.float32(material.specular))
        mainScene.setUniform("material.shininess", numpy.float32(material.shininess))


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
    )
