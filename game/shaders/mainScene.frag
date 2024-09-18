#version 460 core

const vec3 depthColor = vec3(0, 0, 0);

in vec3 Position;
in vec3 Normal;
in vec2 TexCoord;

out vec4 FragColor;

layout (binding = 0) uniform sampler2D ourTexture;
uniform vec3 cameraPosition;
uniform float maxViewDepth;
uniform struct Material
{
    float ambient;
    float diffuse;
    float specular;
    float shininess;
} material;

vec3 getTextureColor()
{
    return texture(ourTexture, TexCoord).xyz;
}

float getViewDepthFactor()
{
    float dist = length(Position - cameraPosition);
    float factor = clamp(dist / maxViewDepth, 0.0, 1.0);

    return factor;
}

void main()
{
    vec3 textureColor = getTextureColor();
    float viewDepthFactor = getViewDepthFactor();

    vec3 shadeColor = mix(textureColor, depthColor, viewDepthFactor);

    FragColor = vec4(shadeColor, 1.0);
}
