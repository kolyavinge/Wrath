from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.gl.VBORenderer import VBORenderer
from game.model.weapon.Plasma import PlasmaBullet
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.weapon.BulletRenderCollection import BulletRenderCollection


class NonStandartBulletRenderer:

    def __init__(self, gameData, renderCollection, shaderProgramCollection, shineCircleRenderer, vboRenderer):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.shineCircleRenderer = shineCircleRenderer
        self.vboRenderer = vboRenderer
        self.shineCircleParams = ShineCircleParams()
        self.shineCircleParams.radius = 0.005
        self.shineCircleParams.shineColor = ColorVector3(85, 239, 247)
        self.shineCircleParams.shineColor.normalize()
        self.shineCircleParams.shineStrength = 2

    def render(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        for bullet in self.gameData.bullets:
            if type(bullet) == PlasmaBullet:
                self.renderPlasmaBullet(bullet)

        glDisable(GL_CULL_FACE)
        glDisable(GL_DEPTH_TEST)

    def renderPlasmaBullet(self, bullet):
        modelMatrix = (
            TransformMatrix4Builder()
            .translate(bullet.currentPosition.x, bullet.currentPosition.y, bullet.currentPosition.z)
            .rotate(self.gameData.player.yawRadians, CommonConstants.zAxis)
            .rotate(self.gameData.player.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(bullet.getModelMatrix())
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        model = self.renderCollection.getRenderModel3d(PlasmaBullet)
        for mesh in model.meshes:
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)
        shader.unuse()


def makeNonStandartBulletRenderer(resolver):
    return NonStandartBulletRenderer(
        resolver.resolve(GameData),
        resolver.resolve(BulletRenderCollection),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(ShineCircleRenderer),
        resolver.resolve(VBORenderer),
    )
