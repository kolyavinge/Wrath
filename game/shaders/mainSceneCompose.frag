#version 460 core

out vec4 FragColor;

uniform sampler2D diffuseSpecularTexture;

void main()
{
    FragColor = texelFetch(diffuseSpecularTexture, ivec2(gl_FragCoord), 0);
}
