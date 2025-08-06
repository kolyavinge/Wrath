#version 460 core

out vec4 FragColor;

layout (binding = 0) uniform sampler2D diffuseSpecularTexture;
layout (binding = 1) uniform sampler2D stencilMaskTexture;

uniform vec2 resolution;

const int offsetsCount = 32;
vec2 offsets[offsetsCount] =
{
    vec2(0.0020833333333333333,0.0),
    vec2(0.00204330266750673,0.0007225567482078824),
    vec2(0.0019247490260651807,0.001417346045796629),
    vec2(0.0017322283589636359,0.0020576675297022304),
    vec2(0.001473139127471974,0.002618914004394621),
    vec2(0.0011574379854575048,0.0030795170826020193),
    vec2(0.0007972571507606038,0.0034217760463380992),
    vec2(0.000406438170866934,0.0036325380755675204),
    vec2(1.2756737491118262e-19,0.003703703703703704),
    vec2(-0.00040643817086693373,0.0036325380755675204),
    vec2(-0.0007972571507606035,0.0034217760463380992),
    vec2(-0.001157437985457504,0.0030795170826020198),
    vec2(-0.0014731391274719738,0.002618914004394621),
    vec2(-0.001732228358963636,0.0020576675297022304),
    vec2(-0.001924749026065181,0.0014173460457966277),
    vec2(-0.0020433026675067303,0.0007225567482078805),
    vec2(-0.0020833333333333333,-2.835976814019963e-18),
    vec2(-0.0020433026675067295,-0.000722556748207886),
    vec2(-0.0019247490260651796,-0.001417346045796633),
    vec2(-0.0017322283589636344,-0.0020576675297022348),
    vec2(-0.0014731391274719716,-0.002618914004394625),
    vec2(-0.0011574379854575015,-0.0030795170826020232),
    vec2(-0.0007972571507605998,-0.003421776046338102),
    vec2(-0.0004064381708669293,-0.0036325380755675217),
    vec2(5.1684129983922344e-18,-0.003703703703703704),
    vec2(0.00040643817086693937,-0.003632538075567518),
    vec2(0.0007972571507606093,-0.003421776046338095),
    vec2(0.0011574379854575102,-0.003079517082602013),
    vec2(0.001473139127471979,-0.002618914004394612),
    vec2(0.00173222835896364,-0.0020576675297022196),
    vec2(0.0019247490260651838,-0.001417346045796616),
    vec2(0.0020433026675067316,-0.000722556748207868)
};

vec4 getBluredShadowCoeff()
{
    vec2 uv = gl_FragCoord.xy / resolution.xy;
    vec4 resultColor = texture(stencilMaskTexture, uv);
    for (int i = 0; i < offsetsCount; i++)
    {
        vec2 offset = offsets[i];
        resultColor += texture(stencilMaskTexture, uv + offset);
    }
    resultColor /= offsetsCount;

    return resultColor;
}

const float piDouble = 6.28318530718;
const float directions = 8.0;
const float quality = 4.0;
const float blurSize = 2.0;
const float piDoubleDivDirections = piDouble / directions;
const float inverseQuality = 1.0 / quality;

vec2 radius = blurSize / resolution.xy;

vec4 getBluredShadowCoeff2()
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
    FragColor = texelFetch(diffuseSpecularTexture, ivec2(gl_FragCoord), 0) * getBluredShadowCoeff2();
}
