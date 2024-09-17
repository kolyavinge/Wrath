#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Normal;
layout (location = 2) in vec2 in_TexCoord;

out vec3 Position;
out vec2 TexCoord;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat4 mvpMatrix;

void main()
{
    Position = in_Position;
    TexCoord = in_TexCoord;
    gl_Position = mvpMatrix * vec4(in_Position, 1.0);
}
