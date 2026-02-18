from game.gl.model3d.AnimationPlayer import PlayableAnimation
from game.model.person.PersonStates import PersonZState
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyAnimationCollection:

    def __init__(
        self,
        renderCollection: EnemyRenderCollection,
    ):
        self.renderCollection = renderCollection
        self.animationNames = {}
        self.animationNames[PersonZState.onFloor] = "group|Take 001|BaseLayer"
        self.animations = {}

    def addPerson(self, person):
        modelAnimations = self.renderCollection.enemyModel.animations
        animationName = self.animationNames[PersonZState.onFloor]
        self.animations[person] = PlayableAnimation(modelAnimations[animationName])

    def getPlayableAnimationOrNone(self, person):
        if person.zState == person.prevZState:
            return self.animations[person]

        if person.zState in self.animationNames:
            modelAnimations = self.renderCollection.enemyModel.animations
            animationName = self.animationNames[person.zState]
            animation = PlayableAnimation(modelAnimations[animationName])
        else:
            animation = None

        self.animations[person] = animation

        return animation
