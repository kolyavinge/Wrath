#version 460 core

const vec4 depthColor = vec4(0.0, 0.0, 0.0, 1.0);

in vec3 PositionView;
in vec3 NormalView;
in vec2 TexCoord;

layout (location = 0) out vec4 out_Ambient;
layout (location = 1) out vec4 out_DiffuseSpecular;

layout (binding = 0) uniform sampler2D ourTexture;
uniform mat4 modelViewMatrix;
uniform float maxDepth;

uniform struct Material
{
    float ambient;
    float diffuse;
    float specular;
    float shininess;
} material;

const int maxLightsCount = 25;
uniform int lightsCount;
uniform struct Light
{
    vec3 color;
    vec3 positionView;
} light[maxLightsCount];

uniform int spotsCount;
uniform struct Spot
{
    vec3 color;
    vec3 positionView;
    vec3 directionView;
    float attenuation;
    float cutoffCos;
} spot[maxLightsCount];

vec4 getTextureColor()
{
    return texture(ourTexture, TexCoord);
}

void getLightColor(int lightIndex, out vec3 ambient, out vec3 diffuseSpecular)
{
    vec3 n = normalize(NormalView);
    vec3 s = normalize(light[lightIndex].positionView - PositionView);
    float sDotN = max(dot(s, n), 0.0);
    float diffuse = material.diffuse * sDotN;
    float specular = 0.0;
    vec3 v = normalize(-PositionView);
    vec3 h = normalize(v + s);
    float hDotN = max(dot(h, n), 0.0);
    specular = material.specular * pow(hDotN, material.shininess);
    ambient += light[lightIndex].color * material.ambient;
    diffuseSpecular += light[lightIndex].color * (diffuse + specular);
}

void getSpotColor(int spotIndex, out vec3 ambient, out vec3 diffuseSpecular)
{
    vec3 n = normalize(NormalView);
    float diffuse = 0.0;
    float specular = 0.0;
    vec3 s = normalize(spot[spotIndex].positionView - PositionView);
    float cosAngle = dot(-s, spot[spotIndex].directionView);
    float spotScale = 0.0;
    if (cosAngle >= spot[spotIndex].cutoffCos)
    {
        spotScale = pow(cosAngle, spot[spotIndex].attenuation);
        float sDotN = max(dot(s, n), 0.0);
        diffuse = material.diffuse * sDotN;
        vec3 v = normalize(-PositionView);
        vec3 h = normalize(v + s);
        float hDotN = max(dot(h, n), 0.0);
        specular = material.specular * pow(hDotN, material.shininess);
    }
    ambient += spot[spotIndex].color * spotScale * material.ambient;
    diffuseSpecular += spot[spotIndex].color * spotScale * (diffuse + specular);
}

void getTotalLightColor(out vec3 ambient, out vec3 diffuseSpecular)
{
    for (int lightIndex = 0; lightIndex < lightsCount; lightIndex++)
    {
        getLightColor(lightIndex, ambient, diffuseSpecular);
    }

    for (int spotIndex = 0; spotIndex < spotsCount; spotIndex++)
    {
        getSpotColor(spotIndex, ambient, diffuseSpecular);
    }
}

float getViewDepthFactor()
{
    return clamp(length(PositionView) / maxDepth, 0.0, 1.0);
}

void main()
{
    vec4 textureColor = getTextureColor();
    vec3 ambient = vec3(0.0);
    vec3 diffuseSpecular = vec3(0.0);
    getTotalLightColor(ambient, diffuseSpecular);
    float viewDepthFactor = getViewDepthFactor();
    out_Ambient = mix(textureColor * vec4(ambient, 1.0), depthColor, viewDepthFactor);
    out_DiffuseSpecular = mix(textureColor * vec4(diffuseSpecular, 1.0), depthColor, viewDepthFactor);
}
