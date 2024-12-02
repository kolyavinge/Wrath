#version 460 core

out vec4 FragColor;

in vec4 Position;
in vec4 Center;

uniform vec2 resolution;
uniform float radius;
uniform vec3 shineColor;
uniform float shineStrength;
uniform float screenAspect;

void main()
{
    vec2 uv = Position.xy - Center.xy;
    uv.x *= screenAspect;
    float dist = length(uv) - radius;
    vec4 color = vec4(step(0.0, -dist));
    float shine = shineStrength / dist;
    shine = clamp(shine, 0.0, 1.0);
    color += shine;
    color *= vec4(shineColor, 1.0);
    FragColor = color;
}
