from game.calc.TransformMatrix4 import TransformMatrix4


class PlayableAnimation:

    def __init__(self, animation):
        self.animation = animation
        self.currentTime = 0.0
        self.boneTransformMatrices = [TransformMatrix4.identity] * animation.allBonesCount


class AnimationPlayer:

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
        transformMatrix = self.getFrameTransformMatrix(channel.translationFrameRoot, currentTime).copy()
        transformMatrix.mul(self.getFrameTransformMatrix(channel.rotationFrameRoot, currentTime))
        transformMatrix.mul(self.getFrameTransformMatrix(channel.scaleFrameRoot, currentTime))

        return transformMatrix

    def getFrameTransformMatrix(self, frameRoot, currentTime):
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

        return resultFrame.transformMatrix


def makeAnimationPlayer(resolver):
    return AnimationPlayer()
