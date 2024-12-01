#version 460 core

out vec4 FragColor;

in vec2 TexCoord;

uniform float alpha;
uniform sampler2D ourTexture;

void main()
{
    FragColor = texture(ourTexture, TexCoord);
    FragColor.w *= alpha;
}
