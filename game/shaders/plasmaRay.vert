#version 460 core

layout (location = 0) in vec3 in_Position;

out vec4 Position;
out vec4 Center;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform vec3 startPosition;

mat4 modelViewProjectionMatrix = projectionMatrix * viewMatrix * modelMatrix;

void main()
{
    Center = modelViewProjectionMatrix * vec4(startPosition, 1.0);
    Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
    gl_Position = Position;
}
