#version 460 core

layout (location = 0) out vec4 FragColor;

layout (binding = 0) uniform sampler2D diffuseSpecularTexture;

void main()
{
    FragColor = texelFetch(diffuseSpecularTexture, ivec2(gl_FragCoord), 0);
}
