#version 460 core

const vec4 depthColor = vec4(0.0, 0.0, 0.0, 1.0);

in vec3 PositionView;
in vec3 NormalView;
in vec2 TexCoord;

out vec4 FragColor;

layout (binding = 0) uniform sampler2D ourTexture;
uniform mat4 modelViewMatrix;
uniform mat3 normalMatrix;
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
    vec3 position;
} light[maxLightsCount];

uniform int spotsCount;
uniform struct Spot
{
    vec3 color;
    vec3 position;
    vec3 direction;
    float attenuation;
    float cutoffCos;
} spot[maxLightsCount];

vec4 getTextureColor()
{
    return texture(ourTexture, TexCoord);
}

vec3 getLightColor(int lightIndex)
{
    vec3 n = normalize(NormalView);
    float ambient = material.ambient;
    vec3 lightPositionView = vec3(modelViewMatrix * vec4(light[lightIndex].position, 1.0));
    vec3 s = normalize(lightPositionView - PositionView);
    float sDotN = max(dot(s, n), 0.0);
    float diffuse = material.diffuse * sDotN;
    float specular = 0.0;
    if (sDotN > 0.0)
    {
        vec3 v = normalize(-PositionView);
        vec3 h = normalize(v + s);
        float hDotN = max(dot(h, n), 0.0);
        specular = material.specular * pow(hDotN, material.shininess);
    }

    return light[lightIndex].color * (ambient + diffuse + specular);
}

vec3 getSpotColor(int spotIndex)
{
    vec3 n = normalize(NormalView);
    float ambient = material.ambient;
    float diffuse = 0.0;
    float specular = 0.0;
    vec3 spotPositionView = vec3(modelViewMatrix * vec4(spot[spotIndex].position, 1.0));
    vec3 s = normalize(spotPositionView - PositionView);
    vec3 lightDirection = normalize(normalMatrix * spot[spotIndex].direction);
    float cosAngle = dot(-s, lightDirection);
    float spotScale = 0.0;
    if (cosAngle >= spot[spotIndex].cutoffCos)
    {
        spotScale = pow(cosAngle, spot[spotIndex].attenuation);
        float sDotN = max(dot(s, n), 0.0);
        diffuse = material.diffuse * sDotN;
        if (sDotN > 0.0)
        {
            vec3 v = normalize(-PositionView);
            vec3 h = normalize(v + s);
            float hDotN = max(dot(h, n), 0.0);
            specular = material.specular * pow(hDotN, material.shininess);
        }
    }

    return spot[spotIndex].color * spotScale * (ambient + diffuse + specular);
}

vec4 getTotalLightColor()
{
    vec3 result = vec3(0.0);

    for (int lightIndex = 0; lightIndex < lightsCount; lightIndex++)
    {
        result += getLightColor(lightIndex);
    }

    for (int spotIndex = 0; spotIndex < spotsCount; spotIndex++)
    {
        result += getSpotColor(spotIndex);
    }

    return vec4(result, 1.0);
}

float getViewDepthFactor()
{
    return clamp(length(PositionView) / maxDepth, 0.0, 1.0);
}

void main()
{
    vec4 textureColor = getTextureColor();
    vec4 lightColor = getTotalLightColor();
    float viewDepthFactor = getViewDepthFactor();
    vec4 shadeColor = mix(textureColor * lightColor, depthColor, viewDepthFactor);
    FragColor = shadeColor;
    FragColor.w = 1.0;
}
