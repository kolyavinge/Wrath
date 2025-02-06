#version 460 core

layout (location = 0) in vec3 in_Position;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

mat4 modelViewProjectionMatrix = projectionMatrix * viewMatrix * modelMatrix;

void main()
{
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
