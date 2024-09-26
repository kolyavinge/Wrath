#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Normal;
layout (location = 2) in vec2 in_TexCoord;

out vec3 PositionView;
out vec3 NormalView;
out vec2 TexCoord;

uniform mat4 modelViewMatrix;
uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

void main()
{
    PositionView = vec3(modelViewMatrix * vec4(in_Position, 1.0));
    NormalView = normalize(normalMatrix * in_Normal);
    TexCoord = in_TexCoord;
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
