from OpenGL.GL import *

from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection
from game.render.level.LevelSegmentVBOCollection import LevelSegmentVBOCollection


class LevelRenderer:

    def __init__(self, gameData, levelSegmentVBOCollection, vboRenderer, shaderProgramCollection, textureCollection):
        self.gameData = gameData
        self.levelSegmentVBOCollection = levelSegmentVBOCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.textureCollection = textureCollection
        self.modelMatrixFloat32Array = TransformMatrix4().toFloat32Array()

    def init(self):
        self.levelSegmentVBOCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())

    def render(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        self.textureCollection.blank.bind(GL_TEXTURE0)
        self.shaderProgramCollection.mainScene.use()
        self.setUniforms()
        self.renderLevelSegments()
        self.shaderProgramCollection.mainScene.unuse()
        self.textureCollection.blank.unbind()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

    def setUniforms(self):
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        self.shaderProgramCollection.mainScene.setUniform("modelMatrix", self.modelMatrixFloat32Array)
        self.shaderProgramCollection.mainScene.setUniform("viewMatrix", camera.viewMatrix.toFloat32Array())
        self.shaderProgramCollection.mainScene.setUniform("projectionMatrix", camera.projectionMatrix.toFloat32Array())
        self.shaderProgramCollection.mainScene.setUniform("mvpMatrix", mvpMatrix.toFloat32Array())

    def renderLevelSegments(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            vbo = self.levelSegmentVBOCollection.getLevelSegmentVBO(levelSegment)
            self.vboRenderer.render(vbo)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelSegmentVBOCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(TextureCollection),
    )
