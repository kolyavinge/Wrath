#version 460 core

layout (location = 0) in vec3 in_Position;

out vec4 Position;

void main()
{
    gl_Position = vec4(in_Position, 1.0);
}
