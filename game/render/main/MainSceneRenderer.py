from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.gl.ext import *
from game.gl.ScreenQuadVBO import ScreenQuadVBO
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelItemGroupCollection import LevelItemGroupCollection
from game.render.level.ShadowCastLevelItemCollection import *


class MainSceneRenderer:

    def __init__(self, gameData, levelItemGroupCollection, shadowCastLevelItemCollection, vboRenderer, shaderProgramCollection, screenQuadVBO):
        self.gameData = gameData
        self.levelItemGroupCollection = levelItemGroupCollection
        self.shadowCastLevelItemCollection = shadowCastLevelItemCollection
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelItemGroupCollection.init(allLevelSegments)
        self.shadowCastLevelItemCollection.init(allLevelSegments)
        # init framebuffer
        self.viewportWidth, self.viewportHeight = glGetViewportSize()
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
        width = self.viewportWidth - 1
        height = self.viewportHeight - 1
        glBlitFramebuffer(0, 0, width, height, 0, 0, width, height, GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT, GL_NEAREST)
        glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
        glDepthMask(GL_FALSE)
        glEnable(GL_DEPTH_CLAMP)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        # stencil test always succeeds, increments for front faces and decrements for back
        glClear(GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glStencilFunc(GL_ALWAYS, 0, 0xFFFF)
        glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_DECR_WRAP, GL_KEEP)
        glStencilOpSeparate(GL_BACK, GL_KEEP, GL_INCR_WRAP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneShadowVolumes
        shader.use()
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setModelViewMatrix(self.gameData.camera.viewMatrix)
        # draw shadow casters
        for levelSegment in self.gameData.visibleLevelSegments:
            # if self.gameData.playerItems.torch.isActive:
            #     shader.setTorchPosition(self.gameData.player.eyePosition)
            #     vbo = self.shadowCastLevelItemCollection.getShadowCastersVBO(levelSegment)
            #     self.vboRenderer.render(vbo)
            for light in levelSegment.lights:
                shader.setLight(light)
                vbo = self.shadowCastLevelItemCollection.getShadowCastersVBO(levelSegment)
                self.vboRenderer.render(vbo)
        shader.unuse()
        glDisable(GL_DEPTH_CLAMP)
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_STENCIL_TEST)

    def composeScene(self):
        glEnable(GL_STENCIL_TEST)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_ONE, GL_ONE)
        glStencilFunc(GL_EQUAL, 0, 0xFFFF)  # render pixels that have a stencil value 0
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneCompose
        shader.use()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.diffuseSpecularTexture)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)
        glDisable(GL_STENCIL_TEST)


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(ShadowCastLevelItemCollection),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(ScreenQuadVBO),
    )
