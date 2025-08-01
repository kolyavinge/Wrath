#version 460 core

out vec4 FragColor;

layout (binding = 0) uniform sampler2D diffuseSpecularTexture;
layout (binding = 1) uniform sampler2D stencilMaskTexture;

void main()
{
    FragColor = texelFetch(diffuseSpecularTexture, ivec2(gl_FragCoord), 0) * texelFetch(stencilMaskTexture, ivec2(gl_FragCoord), 0);
}
