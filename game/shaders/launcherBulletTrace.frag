#version 460 core

in float TransparentValue;

out vec4 FragColor;

uniform vec3 particleColor;

void main()
{
    FragColor = vec4(particleColor, 1.0);
    FragColor.a = TransparentValue;
}
