#version 460 core

layout (location = 0) in vec3 in_Position;

out vec3 Position;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

mat4 modelViewProjectionMatrix = projectionMatrix * viewMatrix * modelMatrix;

void main()
{
    Position = in_Position;
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
