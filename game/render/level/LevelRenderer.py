from OpenGL.GL import *

from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelSegmentVBOCollection import LevelSegmentVBOCollection


class LevelRenderer:

    def __init__(self, gameData, levelSegmentVBOCollection, vboRenderer, shaderProgramCollection):
        self.gameData = gameData
        self.levelSegmentVBOCollection = levelSegmentVBOCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.modelMatrixFloat32Array = TransformMatrix4().toFloat32Array()

    def init(self):
        self.levelSegmentVBOCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())

    def render(self):
        glEnable(GL_DEPTH_TEST)
        for levelSegment in self.gameData.visibleLevelSegments:
            self.renderLevelSegment(levelSegment)
        glDisable(GL_DEPTH_TEST)

    def renderLevelSegment(self, levelSegment):
        vbo = self.levelSegmentVBOCollection.getLevelSegmentVBO(levelSegment)
        self.shaderProgramCollection.mainScene.use()
        self.setUniforms()
        self.vboRenderer.render(vbo)
        self.shaderProgramCollection.mainScene.unuse()

    def setUniforms(self):
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        self.shaderProgramCollection.mainScene.setUniform("modelMatrix", self.modelMatrixFloat32Array)
        self.shaderProgramCollection.mainScene.setUniform("viewMatrix", camera.viewMatrix.toFloat32Array())
        self.shaderProgramCollection.mainScene.setUniform("projectionMatrix", camera.projectionMatrix.toFloat32Array())
        self.shaderProgramCollection.mainScene.setUniform("mvpMatrix", mvpMatrix.toFloat32Array())


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelSegmentVBOCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
    )
