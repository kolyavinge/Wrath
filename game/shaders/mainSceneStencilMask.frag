#version 460 core

layout (location = 2) out vec4 out_StencilMaskTexture;

void main()
{
    out_StencilMaskTexture = vec4(1.0);
}
