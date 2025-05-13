from OpenGL.GL import *

from game.gl.model3d.AnimationPlayer import AnimationPlayer, PlayableAnimation
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.PersonState import PersonState
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(
        self,
        renderCollection: EnemyRenderCollection,
        model3dRenderer: Model3dRenderer,
        animationPlayer: AnimationPlayer,
    ):
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.animationPlayer = animationPlayer
        self.animationNames = {}
        self.animationNames[PersonState.standing] = "group|Take 001|BaseLayer"
        self.animations = {}

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
        if enemy.state == enemy.prevState:
            return self.animations[enemy]

        if enemy.state in self.animationNames:
            animation = PlayableAnimation(model.animations[self.animationNames[enemy.state]])
        else:
            animation = None

        self.animations[enemy] = animation

        return animation


def makeEnemyRenderer(resolver):
    return EnemyRenderer(
        resolver.resolve(EnemyRenderCollection),
        resolver.resolve(Model3dRenderer),
        resolver.resolve(AnimationPlayer),
    )
