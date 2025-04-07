from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.FrameInterpolator import FrameInterpolator


class PlayableAnimation:

    def __init__(self, animation):
        self.animation = animation
        self.currentTime = 0.0
        self.boneTransformMatrices = [TransformMatrix4.identity] * animation.allBonesCount


class AnimationPlayer:

    def __init__(self, frameInterpolator):
        self.frameInterpolator = frameInterpolator

    def update(self, playableAnimation, deltaTime=0.025):
        self.calculateBoneTransformMatrices(playableAnimation, playableAnimation.animation.rootNode, TransformMatrix4.identity)
        playableAnimation.currentTime += playableAnimation.animation.ticksPerSecond * deltaTime
        playableAnimation.currentTime = playableAnimation.currentTime % playableAnimation.animation.duration

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
        translationFrame = self.getFrame(channel.translationFrameRoot, currentTime)
        rotationFrame = self.getFrame(channel.rotationFrameRoot, currentTime)
        scaleFrame = self.getFrame(channel.scaleFrameRoot, currentTime)

        translationValue = self.frameInterpolator.getTranslationValue(translationFrame, currentTime)
        translationMatrix = TransformMatrix4()
        translationMatrix.translate(translationValue.x, translationValue.y, translationValue.z)

        rotationValue = self.frameInterpolator.getRotationValue(rotationFrame, currentTime)
        rotationMatrix = rotationValue.getTransformMatrix4()

        scaleValue = self.frameInterpolator.getScaleValue(scaleFrame, currentTime)
        scaleMatrix = TransformMatrix4()
        scaleMatrix.scale(scaleValue.x, scaleValue.y, scaleValue.z)

        transformMatrix = TransformMatrix4()
        transformMatrix.setIdentity()
        transformMatrix.mul(translationMatrix)
        transformMatrix.mul(rotationMatrix)
        transformMatrix.mul(scaleMatrix)

        return transformMatrix

    def getFrame(self, frameRoot, currentTime):
        node = frameRoot

        while True:
            if node is None:
                break
            elif currentTime == node.time:
                resultFrame = node
                break
            elif currentTime < node.time:
                node = node.leftChild
            else:
                resultFrame = node
                node = node.rightChild

        assert resultFrame is not None

        return resultFrame


def makeAnimationPlayer(resolver):
    return AnimationPlayer(resolver.resolve(FrameInterpolator))
