#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Normal;
layout (location = 2) in vec2 in_TexCoord;
layout (location = 4) in ivec4 boneIds;
layout (location = 5) in vec4 weights;

out vec3 PositionView;
out vec3 NormalView;
out vec2 TexCoord;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

const int maxBonesCount = 100;
const int maxBonesCountInfluence = 4;
uniform bool hasAnimation;
uniform mat4 boneTransformMatrices[maxBonesCount];

mat4 modelViewMatrix = viewMatrix * modelMatrix;
mat4 modelViewProjectionMatrix = projectionMatrix * modelViewMatrix;
mat3 normalMatrix = mat3(modelViewMatrix);

void processWithAnimation()
{
    mat4 boneTransform = mat4(0.0);
    for (int i = 0; i < maxBonesCountInfluence; i++)
    {
        if (weights[i] > 0.0)
        {
            boneTransform += boneTransformMatrices[boneIds[i]] * weights[i];
        }
    }
    PositionView = vec3(modelViewMatrix * boneTransform * vec4(in_Position, 1.0));
    NormalView = normalize(normalMatrix * vec3(boneTransform * vec4(in_Normal, 1.0)));
    TexCoord = in_TexCoord;
    gl_Position = modelViewProjectionMatrix * boneTransform * vec4(in_Position, 1.0);
}

void processDefault()
{
    PositionView = vec3(modelViewMatrix * vec4(in_Position, 1.0));
    NormalView = normalize(normalMatrix * in_Normal);
    TexCoord = in_TexCoord;
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
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
