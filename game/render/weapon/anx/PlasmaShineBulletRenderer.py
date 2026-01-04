from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.engine.GameState import GameState
from game.gl.ColorVector3 import ColorVector3
from game.render.anx.ShineCircleRenderer import ShineCircleParams, ShineCircleRenderer


class PlasmaShineBulletRenderer:

    def __init__(
        self,
        gameState: GameState,
        shineCircleRenderer: ShineCircleRenderer,
    ):
        self.gameState = gameState
        self.shineCircleRenderer = shineCircleRenderer
        self.shineCircleParams = ShineCircleParams()
        self.shineCircleParams.radius = 0.09
        self.shineCircleParams.shineColor = ColorVector3(85, 239, 247)
        self.shineCircleParams.shineColor.normalize()
        self.shineCircleParams.shineStrength = 0.04

    def renderBullet(self, bullet):
        modelMatrix = (
            TransformMatrix4Builder()
            .translate(bullet.currentPosition.x, bullet.currentPosition.y, bullet.currentPosition.z)
            .rotate(self.gameState.player.yawRadians, CommonConstants.zAxis)
            .rotate(self.gameState.player.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
        self.shineCircleRenderer.render(modelMatrix, self.shineCircleParams)
