from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.model.weapon.Plasma import PlasmaBullet
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer


class ShineBulletRenderer:

    def __init__(self, gameData, shineCircleRenderer):
        self.gameData = gameData
        self.shineCircleRenderer = shineCircleRenderer
        self.plasmaShineParams = ShineCircleParams()
        self.plasmaShineParams.radius = 0.005
        self.plasmaShineParams.shineColor = ColorVector3(85, 239, 247)
        self.plasmaShineParams.shineColor.normalize()
        self.plasmaShineParams.shineStrength = 2
        self.renderFuncs = {}
        self.renderFuncs[PlasmaBullet] = self.renderPlasmaBullet

    def render(self):
        glEnable(GL_DEPTH_TEST)
        for bullet in self.gameData.bullets:
            if type(bullet) in self.renderFuncs:
                self.renderFuncs[type(bullet)](bullet)
        glDisable(GL_DEPTH_TEST)

    def renderPlasmaBullet(self, bullet):
        modelMatrix = (
            TransformMatrix4Builder()
            .translate(bullet.currentPosition.x, bullet.currentPosition.y, bullet.currentPosition.z)
            .rotate(self.gameData.player.yawRadians, CommonConstants.zAxis)
            .rotate(self.gameData.player.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
        self.shineCircleRenderer.render(modelMatrix, self.plasmaShineParams)


def makeShineBulletRenderer(resolver):
    return ShineBulletRenderer(
        resolver.resolve(GameData),
        resolver.resolve(ShineCircleRenderer),
    )
