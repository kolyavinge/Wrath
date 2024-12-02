from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer


class PlasmaShineBulletRenderer:

    def __init__(self, gameData, shineCircleRenderer):
        self.gameData = gameData
        self.shineCircleRenderer = shineCircleRenderer
        self.shineCircleParams = ShineCircleParams()
        self.shineCircleParams.radius = 0.005
        self.shineCircleParams.shineColor = ColorVector3(85, 239, 247)
        self.shineCircleParams.shineColor.normalize()
        self.shineCircleParams.shineStrength = 0.02

    def renderBullet(self, bullet):
        modelMatrix = (
            TransformMatrix4Builder()
            .translate(bullet.currentPosition.x, bullet.currentPosition.y, bullet.currentPosition.z)
            .rotate(self.gameData.player.yawRadians, CommonConstants.zAxis)
            .rotate(self.gameData.player.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams)


def makePlasmaShineBulletRenderer(resolver):
    return PlasmaShineBulletRenderer(
        resolver.resolve(GameData),
        resolver.resolve(ShineCircleRenderer),
    )
