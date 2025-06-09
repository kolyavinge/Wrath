from game.engine.GameData import GameData
from game.gl.model3d.AnimationPlayer import PlayableAnimation
from game.model.person.PersonZState import PersonZState
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyAnimationCollection:

    def __init__(
        self,
        gameData: GameData,
        renderCollection: EnemyRenderCollection,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.animationNames = {}
        self.animationNames[PersonZState.onFloor] = "group|Take 001|BaseLayer"
        self.animations = {}

    def init(self):
        for enemy in self.gameData.enemies:
            self.initForEnemy(enemy)

    def initForEnemy(self, enemy):
        modelAnimations = self.renderCollection.enemyModel.animations
        animationName = self.animationNames[PersonZState.onFloor]
        self.animations[enemy] = PlayableAnimation(modelAnimations[animationName])

    def getPlayableAnimationOrNone(self, enemy):
        if enemy.zState == enemy.prevZState:
            return self.animations[enemy]

        if enemy.zState in self.animationNames:
            modelAnimations = self.renderCollection.enemyModel.animations
            animationName = self.animationNames[enemy.zState]
            animation = PlayableAnimation(modelAnimations[animationName])
        else:
            animation = None

        self.animations[enemy] = animation

        return animation
