from OpenGL.GL import *

from game.gl.model3d.AnimationPlayer import AnimationPlayer, PlayableAnimation
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.PersonState import PersonState
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(self, renderCollection, model3dRenderer, animationPlayer):
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.animationPlayer = animationPlayer
        self.animation = None

    def render(self, shader, levelSegment):
        model = self.renderCollection.enemyModel
        for enemy in levelSegment.enemies:
            shader.setModelMatrix(enemy.getModelMatrix())
            animation = self.getPlayableAnimationOrNone(enemy, model)
            if animation is not None:
                self.animationPlayer.update(animation)
                shader.hasAnimation(True)
                shader.setBoneTransformMatrices(animation.boneTransformMatrices)
            self.model3dRenderer.render(model, shader)
            shader.hasAnimation(False)

    def getPlayableAnimationOrNone(self, enemy, model):
        if self.animation is None:
            if enemy.state == PersonState.standing:
                animation = model.animations["group|standing"]
                self.animation = PlayableAnimation(animation)
                return self.animation
        else:
            return self.animation

        return None


def makeEnemyRenderer(resolver):
    return EnemyRenderer(resolver.resolve(EnemyRenderCollection), resolver.resolve(Model3dRenderer), resolver.resolve(AnimationPlayer))
