#version 460 core

out vec4 FragColor;

in vec2 TexCoord;
in vec4 Color;

uniform sampler2D ourTexture;

void main()
{
    FragColor = texture(ourTexture, TexCoord);
    FragColor.x *= Color.x;
    FragColor.y *= Color.y;
    FragColor.z *= Color.z;
    FragColor.w *= Color.w;
}
