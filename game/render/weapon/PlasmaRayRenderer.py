from OpenGL.GL import *

from game.calc.PlaneOrientationLogic import PlaneOrientationLogic
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.gl.BufferIndices import BufferIndices
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID
from game.gl.TexturedFramebuffer import TexturedFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.Query import Query
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class PlasmaRayRenderer:

    def __init__(
        self,
        gameData: GameState,
        planeOrientationLogic: PlaneOrientationLogic,
        shaderProgramCollection: ShaderProgramCollection,
        vboUpdaterFactory: VBOUpdaterFactory,
        vboRenderer: VBORenderer,
        screenQuadVBO: ScreenQuadVBO,
    ):
        self.gameData = gameData
        self.planeOrientationLogic = planeOrientationLogic
        self.shaderProgramCollection = shaderProgramCollection
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.vboRenderer = vboRenderer
        self.screenQuadVBO = screenQuadVBO
        self.rayFramebuffer = TexturedFramebuffer()
        self.rayFramebuffer.init(1024, 1024)
        rayCount = 1
        self.vbo = self.vboUpdater.buildUnfilled(4 * rayCount, 2 * rayCount, [BufferIndices.vertices, BufferIndices.texCoords, BufferIndices.faces])

    def renderRays(self, rays):
        ethalonRay = Query(rays).firstOrNone(lambda r: r.ownerPerson == self.gameData.player) or rays[0]
        self.renderEthalonRayToFramebuffer(ethalonRay)
        self.renderAllRaysBasedOnEthalon(rays)

    def renderEthalonRayToFramebuffer(self, ray):
        glBindFramebuffer(GL_FRAMEBUFFER, self.rayFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        shader = self.shaderProgramCollection.plasmaRay
        shader.use()
        shader.setResolution(self.rayFramebuffer.textureWidth, self.rayFramebuffer.textureHeight)
        shader.setInitTimeSec(ray.initTimeSec)
        shader.setCurrentTimeSec(self.gameData.globalTimeSec)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)

    def renderAllRaysBasedOnEthalon(self, rays):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.rayFramebuffer.texture)
        for ray in rays:
            vertices = self.planeOrientationLogic.getVerticesOrientedToCamera(
                ray.startPosition, ray.currentPosition, ray.direction, self.gameData.camera.position, 0.15
            )
            self.vbo.reset()
            self.addVerticesToVBO(vertices)
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

        self.vboUpdater.addTexCoord(1, 0)
        self.vboUpdater.addTexCoord(1, 1)
        self.vboUpdater.addTexCoord(0, 1)
        self.vboUpdater.addTexCoord(0, 0)

        self.vboUpdater.addFace(0, 1, 2)
        self.vboUpdater.addFace(0, 2, 3)

        self.vboUpdater.endUpdate()
