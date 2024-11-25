from OpenGL.GL import *

from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
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
        self.shineCircleParams.radius = 0.1
        self.shineCircleParams.shineColor = Vector3(1.0, 1.0, 0.0)
        self.shineCircleParams.shineStrength = 1

    def render(self):
        for bullet in self.gameData.bullets:
            if type(bullet) == PlasmaBullet:
                self.renderPlasmaBullet(bullet)

    def renderPlasmaBullet(self, bullet):
        modelMatrix = bullet.getModelMatrix()
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams)
        shader = self.shaderProgramCollection.texture
        shader.use()
        shader.setModelMatrix(modelMatrix)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        model = self.renderCollection.getRenderModel3d(PlasmaBullet)
        for mesh in model.meshes:
            shader.setMaterial(mesh.material)
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
