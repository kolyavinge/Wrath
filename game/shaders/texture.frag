#version 460 core

layout (location = 0) out vec4 FragColor;

in vec2 TexCoord;

uniform float alpha;

layout (location = 0) uniform sampler2D ourTexture;

void main()
{
    FragColor = texture(ourTexture, TexCoord);
    FragColor.w *= alpha;
}
