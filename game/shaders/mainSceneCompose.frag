#version 460 core

out vec4 FragColor;

layout (binding = 0) uniform sampler2D diffuseSpecularTexture;
layout (binding = 1) uniform sampler2D stencilMaskTexture;

uniform vec2 resolution;

const float piDouble = 6.28318530718;
const float directions = 8.0;
const float quality = 4.0;
const float blurSize = 4.0;
const float piDoubleDivDirections = piDouble / directions;
const float inverseQuality = 1.0 / quality;

vec2 radius = blurSize / resolution.xy;

vec4 getBluredShadowCoeff()
{
    vec2 uv = gl_FragCoord.xy / resolution.xy;
    vec4 resultColor = texture(stencilMaskTexture, uv);
    for (float d = 0.0; d < piDouble; d += piDoubleDivDirections)
    {
        vec2 n = vec2(cos(d), sin(d)) * radius;
        for (float i = inverseQuality; i <= 1.0; i += inverseQuality)
        {
            resultColor += texture(stencilMaskTexture, uv + n * i);
        }
    }

    resultColor /= quality * directions - (directions - 1.0);

    return resultColor;
}

void main()
{
    FragColor = texelFetch(diffuseSpecularTexture, ivec2(gl_FragCoord), 0) * getBluredShadowCoeff();
}
