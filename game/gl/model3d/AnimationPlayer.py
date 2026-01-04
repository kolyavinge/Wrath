from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.gl.model3d.FrameInterpolator import FrameInterpolator


class PlayableAnimation:

    def __init__(self, animation):
        self.animation = animation
        self.currentTime = 0.0
        self.lastGlobalTimeMsec = 0.0
        self.boneTransformMatrices = [TransformMatrix4.identity] * animation.allBonesCount


class AnimationPlayer:

    def __init__(
        self,
        gameState: GameState,
        frameInterpolator: FrameInterpolator,
    ):
        self.gameState = gameState
        self.frameInterpolator = frameInterpolator

    def update(self, playableAnimation, deltaTimeFactor=0.001):
        self.calculateBoneTransformMatrices(playableAnimation, playableAnimation.animation.rootNode, TransformMatrix4.identity)
        deltaTime = self.gameState.globalTimeMsec - playableAnimation.lastGlobalTimeMsec
        playableAnimation.currentTime += playableAnimation.animation.ticksPerSecond * (deltaTime * deltaTimeFactor)
        playableAnimation.currentTime %= playableAnimation.animation.duration
        playableAnimation.lastGlobalTimeMsec = self.gameState.globalTimeMsec

    def calculateBoneTransformMatrices(self, playableAnimation, node, parentTransformMatrix):
        bone = None
        if node.name in playableAnimation.animation.channels:
            channel = playableAnimation.animation.channels[node.name]
            bone = channel.node.bone
            transformMatrix = self.getChannelTransformMatrix(channel, playableAnimation.currentTime)
        else:
            transformMatrix = node.transformMatrix

        globalTransformMatrix = parentTransformMatrix.copy()
        globalTransformMatrix.mul(transformMatrix)

        if bone is not None:
            playableAnimation.boneTransformMatrices[bone.id] = globalTransformMatrix.copy()
            playableAnimation.boneTransformMatrices[bone.id].mul(bone.offsetMatrix)

        for child in node.children:
            self.calculateBoneTransformMatrices(playableAnimation, child, globalTransformMatrix)

    def getChannelTransformMatrix(self, channel, currentTime):
        translationFrame = self.getFrame(channel.translationRootFrame, currentTime)
        rotationFrame = self.getFrame(channel.rotationRootFrame, currentTime)
        scaleFrame = self.getFrame(channel.scaleRootFrame, currentTime)

        translationVector = self.frameInterpolator.getTranslationVector(translationFrame, currentTime)
        translationMatrix = TransformMatrix4()
        translationMatrix.translate(translationVector.x, translationVector.y, translationVector.z)

        rotationQuaternion = self.frameInterpolator.getRotationQuaternion(rotationFrame, currentTime)
        rotationMatrix = rotationQuaternion.getTransformMatrix4()

        scaleVector = self.frameInterpolator.getScaleVector(scaleFrame, currentTime)
        scaleMatrix = TransformMatrix4()
        scaleMatrix.scale(scaleVector.x, scaleVector.y, scaleVector.z)

        transformMatrix = TransformMatrix4()
        transformMatrix.setIdentity()
        transformMatrix.mul(translationMatrix)
        transformMatrix.mul(rotationMatrix)
        transformMatrix.mul(scaleMatrix)

        return transformMatrix

    def getFrame(self, frameRoot, currentTime):
        node = frameRoot

        while node is not None:
            if currentTime == node.time:
                resultFrame = node
                break
            elif currentTime < node.time:
                node = node.leftChild
            else:
                resultFrame = node
                node = node.rightChild

        assert resultFrame is not None

        return resultFrame
