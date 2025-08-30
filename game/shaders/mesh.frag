#version 460 core

out vec4 FragColor;

in vec2 TexCoord;

uniform float colorFactor;
uniform float alphaFactor;
uniform sampler2D ourTexture;

void main()
{
    FragColor = texture(ourTexture, TexCoord);
    FragColor.x *= colorFactor;
    FragColor.y *= colorFactor;
    FragColor.z *= colorFactor;
    FragColor.w *= alphaFactor;
}
