#version 460 core

in vec3 PositionView;
in vec3 NormalView;
in vec2 TexCoord;

layout (location = 0) out vec4 out_Ambient;
layout (location = 1) out vec4 out_DiffuseSpecular;

layout (binding = 0) uniform sampler2D ourTexture;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform float maxDepth;

mat4 modelViewMatrix = viewMatrix * modelMatrix;
mat3 normalMatrix = mat3(modelViewMatrix);

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
    vec3 position;
} lights[maxLightsCount];

uniform int spotsCount;
uniform struct Spot
{
    vec3 color;
    vec3 position;
    vec3 direction;
    float attenuation;
    float cutoffCos;
} spots[maxLightsCount];

vec4 getTextureColor()
{
    return texture(ourTexture, TexCoord);
}

void getLightColor(int lightIndex, inout vec3 ambient, inout vec3 diffuseSpecular)
{
    vec3 n = normalize(NormalView);
    vec3 positionView = vec3(modelViewMatrix * vec4(lights[lightIndex].position, 1.0));
    vec3 s = normalize(positionView - PositionView);
    float sDotN = max(dot(s, n), 0.0);
    float diffuse = material.diffuse * sDotN;
    float specular = 0.0;
    vec3 v = normalize(-PositionView);
    vec3 h = normalize(v + s);
    float hDotN = max(dot(h, n), 0.0);
    specular = material.specular * pow(hDotN, material.shininess);
    ambient += lights[lightIndex].color * material.ambient;
    diffuseSpecular += lights[lightIndex].color * (diffuse + specular);
}

void getSpotColor(int spotIndex, inout vec3 ambient, inout vec3 diffuseSpecular)
{
    vec3 n = normalize(NormalView);
    float diffuse = 0.0;
    float specular = 0.0;
    vec3 positionView = vec3(modelViewMatrix * vec4(spots[spotIndex].position, 1.0));
    vec3 directionView = normalMatrix * spots[spotIndex].direction;
    vec3 s = normalize(positionView - PositionView);
    float cosAngle = dot(-s, directionView);
    float spotScale = 0.0;
    if (cosAngle >= spots[spotIndex].cutoffCos)
    {
        spotScale = pow(cosAngle, spots[spotIndex].attenuation);
        float sDotN = max(dot(s, n), 0.0);
        diffuse = material.diffuse * sDotN;
        vec3 v = normalize(-PositionView);
        vec3 h = normalize(v + s);
        float hDotN = max(dot(h, n), 0.0);
        specular = material.specular * pow(hDotN, material.shininess);
    }
    ambient += spots[spotIndex].color * spotScale * material.ambient;
    diffuseSpecular += spots[spotIndex].color * spotScale * (diffuse + specular);
}

void getTotalLightColor(inout vec3 ambient, inout vec3 diffuseSpecular)
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
    return 1.0 - clamp(length(PositionView) / maxDepth, 0.0, 1.0);
}

void main()
{
    vec4 textureColor = getTextureColor();
    vec3 ambient = vec3(0.0);
    vec3 diffuseSpecular = vec3(0.0);
    getTotalLightColor(ambient, diffuseSpecular);
    vec4 depthColor = vec4(vec3(getViewDepthFactor()), 1.0);
    out_Ambient = textureColor * vec4(ambient, 1.0) * depthColor;
    out_DiffuseSpecular = textureColor * vec4(diffuseSpecular, 1.0) * depthColor;
}
