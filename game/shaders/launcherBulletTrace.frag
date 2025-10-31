#version 460 core

in vec3 ParticleColor;
in float TransparentValue;

out vec4 FragColor;

void main()
{
    FragColor = vec4(ParticleColor, TransparentValue);
}
