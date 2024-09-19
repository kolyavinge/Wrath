#version 460 core

const vec4 depthColor = vec4(0.0, 0.0, 0.0, 1.0);

in vec3 Position;
in vec3 PositionView;
in vec3 NormalView;
in vec2 TexCoord;

out vec4 FragColor;

layout (binding = 0) uniform sampler2D ourTexture;
uniform mat4 modelViewMatrix;
uniform vec3 cameraPosition;
uniform float maxViewDepth;

uniform struct Material
{
    float ambient;
    float diffuse;
    float specular;
    float shininess;
} material;

const int maxLightsCount = 100;
uniform int lightsCount;
uniform struct Light
{
    vec3 position;
    vec3 color;
} light[maxLightsCount];

vec4 getTextureColor()
{
    return texture(ourTexture, TexCoord);
}

vec4 getLightColorFor(int lightIndex)
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

    return vec4(light[lightIndex].color * (ambient + diffuse + specular), 1.0);
}

vec4 getLightColor()
{
    vec4 result = vec4(0.0);
    for (int lightIndex = 0; lightIndex < lightsCount; lightIndex++)
    {
        result += getLightColorFor(lightIndex);
    }

    return result;
}

float getViewDepthFactor()
{
    float dist = length(Position - cameraPosition);
    float factor = clamp(dist / maxViewDepth, 0.0, 1.0);

    return factor;
}

void main()
{
    vec4 textureColor = getTextureColor();
    vec4 lightColor = getLightColor();
    float viewDepthFactor = getViewDepthFactor();
    vec4 shadeColor = mix(textureColor * lightColor, depthColor, viewDepthFactor);
    FragColor = shadeColor;
    FragColor.w = 1.0;
}
