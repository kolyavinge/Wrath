#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Normal;
layout (location = 2) in vec2 in_TexCoord;

out vec3 Position;
out vec3 Normal;
out vec2 TexCoord;

uniform mat4 modelMatrix;
uniform mat4 modelViewMatrix;
uniform mat4 modelViewProjectionMatrix;
uniform mat4 normalMatrix;

void main()
{
    Position = in_Position;
    Normal = in_Normal;
    TexCoord = in_TexCoord;
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
