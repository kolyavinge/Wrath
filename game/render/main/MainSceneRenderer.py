from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.gl.ext import glGetViewportSize
from game.gl.ScreenQuadVBO import ScreenQuadVBO
from game.gl.VBOBuilder import VBOBuilder
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelItemGroupCollection import LevelItemGroupCollection


class MainSceneRenderer:

    def __init__(self, gameData, levelItemGroupCollection, vboRenderer, shaderProgramCollection, screenQuadVBO):
        self.gameData = gameData
        self.levelItemGroupCollection = levelItemGroupCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO

    def init(self):
        self.viewportWidth, self.viewportHeight = glGetViewportSize()
        self.levelItemGroupCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())
        # init framebuffer
        depthBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, depthBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self.viewportWidth, self.viewportHeight)
        ambientBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, ambientBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_RGBA, self.viewportWidth, self.viewportHeight)
        self.diffuseSpecularTexture = glGenTextures(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.diffuseSpecularTexture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, self.viewportWidth, self.viewportHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        self.colorDepthFBO = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.colorDepthFBO)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, depthBuffer)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_RENDERBUFFER, ambientBuffer)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT1, GL_TEXTURE_2D, self.diffuseSpecularTexture, 0)
        glDrawBuffers(2, [GL_COLOR_ATTACHMENT0, GL_COLOR_ATTACHMENT1])
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glBindTexture(GL_TEXTURE_2D, 0)

    def render(self):
        self.calculateLightComponents()
        self.calculateShadowVolumes()
        self.composeScene()

    def calculateLightComponents(self):
        glDepthMask(GL_TRUE)
        glDisable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glBindFramebuffer(GL_FRAMEBUFFER, self.colorDepthFBO)
        glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
        shader = self.shaderProgramCollection.mainSceneLightComponents
        shader.use()
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        shader.setModelViewMatrix(camera.viewMatrix)
        shader.setModelViewProjectionMatrix(mvpMatrix)
        shader.setNormalMatrix(camera.viewMatrix.toMatrix3())
        shader.setMaxDepth(CommonConstants.maxDepth)
        self.renderLevelSegments(shader)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

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
        # copy depth and color buffers from colorDepthFBO to default FBO
        glBindFramebuffer(GL_READ_FRAMEBUFFER, self.colorDepthFBO)
        glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)
        glBlitFramebuffer(
            0,
            0,
            self.viewportWidth - 1,
            self.viewportHeight - 1,
            0,
            0,
            self.viewportWidth - 1,
            self.viewportHeight - 1,
            GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT,
            GL_NEAREST,
        )
        glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
        glDepthMask(GL_FALSE)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        # stencil test always succeeds, increments for front faces and decrements for back
        glClear(GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)
        glStencilFunc(GL_ALWAYS, 0, 0xFFFF)
        glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_KEEP, GL_INCR_WRAP)
        glStencilOpSeparate(GL_BACK, GL_KEEP, GL_KEEP, GL_DECR_WRAP)
        torch = self.gameData.playerItems.torch
        player = self.gameData.player
        allVisibleLights = set()
        for levelSegment in self.gameData.visibleLevelSegments:
            allVisibleLights.update(levelSegment.lights)
        shader = self.shaderProgramCollection.mainSceneShadowVolumes
        shader.use()
        shader.setLight(allVisibleLights, player, torch)
        # draw Shadow Casters
        for levelSegment in self.gameData.visibleLevelSegments:
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                glBindVertexArray(item.vbo.vaoId)
                glDrawElements(GL_TRIANGLES_ADJACENCY, 8 * item.vbo.elementsCount, GL_UNSIGNED_INT, None)
                glBindVertexArray(0)
        shader.unuse()
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)

    def composeScene(self):
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_ONE, GL_ONE)
        # render pixels that have a stencil value 0
        glStencilFunc(GL_EQUAL, 0, 0xFFFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneCompose
        shader.use()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.diffuseSpecularTexture)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(ScreenQuadVBO),
    )