from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.model3d.AnimationPlayer import AnimationPlayer, PlayableAnimation
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.PersonZState import PersonZState
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(
        self,
        gameData: GameData,
        renderCollection: EnemyRenderCollection,
        model3dRenderer: Model3dRenderer,
        animationPlayer: AnimationPlayer,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.animationPlayer = animationPlayer
        self.animationNames = {}
        self.animationNames[PersonZState.onFloor] = "group|Take 001|BaseLayer"
        self.animations = {}

    def render(self, shader, levelSegment):
        for enemy in levelSegment.enemies:
            if self.isEnemyVisible(enemy):
                self.renderEnemy(enemy, shader)

    def renderEnemy(self, enemy, shader):
        model = self.renderCollection.enemyModel
        shader.setModelMatrix(enemy.getModelMatrix())
        animation = self.getPlayableAnimationOrNone(enemy, model)
        if animation is not None:
            self.animationPlayer.update(animation)
            shader.hasAnimation(True)
            shader.setBoneTransformMatrices(animation.boneTransformMatrices)
        self.model3dRenderer.render(model, shader)
        shader.hasAnimation(False)

    def isEnemyVisible(self, enemy):
        enemyDirection = self.gameData.camera.position.getDirectionTo(enemy.middleCenterPoint)
        dotProduct = self.gameData.camera.lookDirection.dotProduct(enemyDirection)
        if dotProduct < 0:
            return False
        dotProduct /= enemyDirection.getLength()
        isVisible = self.gameData.camera.horizontalViewRadiansHalfCos < dotProduct

        return isVisible

    def getPlayableAnimationOrNone(self, enemy, model):
        if enemy.zState == enemy.prevZState:
            return self.animations[enemy]

        if enemy.zState in self.animationNames:
            animation = PlayableAnimation(model.animations[self.animationNames[enemy.zState]])
        else:
            animation = None

        self.animations[enemy] = animation

        return animation
