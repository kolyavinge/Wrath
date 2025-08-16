#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 4) in ivec4 in_BoneIds;
layout (location = 5) in vec4 in_Weights;

out vec3 PositionView;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;

const int maxBonesCount = 100;
const int maxBonesCountInfluence = 4;
uniform bool hasAnimation;
uniform mat4 boneTransformMatrices[maxBonesCount];

mat4 modelViewMatrix = viewMatrix * modelMatrix;

void processWithAnimation()
{
    mat4 boneTransform = mat4(0.0);
    for (int i = 0; i < maxBonesCountInfluence; i++)
    {
        if (in_Weights[i] > 0.0)
        {
            boneTransform += boneTransformMatrices[in_BoneIds[i]] * in_Weights[i];
        }
    }
    PositionView = vec3(modelViewMatrix * boneTransform * vec4(in_Position, 1.0));
}

void processDefault()
{
    PositionView = vec3(modelViewMatrix * vec4(in_Position, 1.0));
}

void main()
{
    if (hasAnimation)
    {
        processWithAnimation();
    }
    else
    {
        processDefault();
    }
}
