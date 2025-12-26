from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.PlaneOrientationLogic import PlaneOrientationLogic
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.gl.BufferIndices import BufferIndices
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class PlasmaRayRenderer:

    def __init__(
        self,
        gameData: GameData,
        planeOrientationLogic: PlaneOrientationLogic,
        shaderProgramCollection: ShaderProgramCollection,
        vboUpdaterFactory: VBOUpdaterFactory,
        vboRenderer: VBORenderer,
    ):
        self.gameData = gameData
        self.planeOrientationLogic = planeOrientationLogic
        self.shaderProgramCollection = shaderProgramCollection
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.vboRenderer = vboRenderer
        self.vbo = self.vboUpdater.buildUnfilled(
            4 * CommonConstants.maxRaysCount, 2 * CommonConstants.maxRaysCount, [BufferIndices.vertices, BufferIndices.faces]
        )

    def renderRays(self, rays):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        shader = self.shaderProgramCollection.plasmaRay
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setResolution(2000, 0)
        shader.setCurrentTimeSec(self.gameData.globalTimeSec)
        for ray in rays:
            vertices = self.planeOrientationLogic.getVerticesOrientedToCamera(
                ray.startPosition,
                ray.currentPosition,
                ray.direction,
                self.gameData.camera.position,
            )
            self.vbo.reset()
            self.addVerticesToVBO(vertices)
            shader.setStartPosition(ray.startPosition)
            shader.setInitTimeSec(ray.initTimeSec)
            self.vboRenderer.render(self.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def addVerticesToVBO(self, vertices):
        self.vboUpdater.beginUpdate(self.vbo)

        self.vboUpdater.addVertex(vertices[0])
        self.vboUpdater.addVertex(vertices[1])
        self.vboUpdater.addVertex(vertices[2])
        self.vboUpdater.addVertex(vertices[3])

        self.vboUpdater.addFace(0, 1, 2)
        self.vboUpdater.addFace(1, 3, 2)

        self.vboUpdater.endUpdate()
