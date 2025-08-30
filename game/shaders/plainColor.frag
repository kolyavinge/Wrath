#version 460 core

out vec4 FragColor;

uniform vec3 color;
uniform float alphaFactor;

void main()
{
    FragColor = vec4(color, 1.0);
    FragColor.w *= alphaFactor;
}
