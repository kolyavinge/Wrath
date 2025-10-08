#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 2) in vec2 in_TexCoord;
layout (location = 3) in vec4 in_Color;

out vec2 TexCoord;
out vec4 Color;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

mat4 modelViewProjectionMatrix = projectionMatrix * viewMatrix * modelMatrix;

void main()
{
    TexCoord = in_TexCoord;
    Color = in_Color;
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
