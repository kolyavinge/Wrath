#version 460 core

layout (location = 0) in vec3 in_Position;

out vec3 PositionView;

uniform mat4 modelViewMatrix;
uniform mat4 modelViewProjectionMatrix;

void main()
{
    PositionView = vec3(modelViewMatrix * vec4(in_Position, 1.0));
    gl_Position = modelViewProjectionMatrix * vec4(in_Position, 1.0);
}
