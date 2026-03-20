from game.anx.CommonConstants import CommonConstants
from game.lib.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer
from game.render.gl.ColorVector3 import ColorVector3


class PlasmaShineBulletRenderer:

    def __init__(
        self,
        shineCircleRenderer: ShineCircleRenderer,
    ):
        self.shineCircleRenderer = shineCircleRenderer
        self.shineCircleParams = ShineCircleParams()
        self.shineCircleParams.radius = 0.09
        self.shineCircleParams.shineColor = ColorVector3(85, 239, 247)
        self.shineCircleParams.shineColor.normalize()
        self.shineCircleParams.shineStrength = 0.04

    def renderBullet(self, bullet, player, camera):
        modelMatrix = (
            TransformMatrix4Builder()
            .translate(bullet.currentPosition.x, bullet.currentPosition.y, bullet.currentPosition.z)
            .rotate(player.yawRadians, CommonConstants.zAxis)
            .rotate(player.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams, camera)
