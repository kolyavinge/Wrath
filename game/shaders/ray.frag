#version 460 core

out vec4 FragColor;

in vec3 Position;
in flat int RayIndex;

const int maxRaysCount = 100;

uniform vec3 origins[maxRaysCount];
uniform vec3 mainAxes[maxRaysCount];
uniform float rayLengths[maxRaysCount];
uniform float rayHeight;
uniform vec3 rayColor;
uniform float rayBrightnesses[maxRaysCount];
uniform float shineStrength;

void main()
{
    vec3 positionDirection = Position - origins[RayIndex];
    float projectedLength = dot(mainAxes[RayIndex], positionDirection);
    vec3 projectedPosition = projectedLength * mainAxes[RayIndex] + origins[RayIndex];
    vec3 heightDirection = Position - projectedPosition;
    float height = length(heightDirection) - rayHeight;
    vec4 color = vec4(step(0.0, -height));
    float shine = shineStrength / height;
    shine = clamp(shine, 0.0, 1.0);
    color += shine;
    color *= vec4(rayColor, 1.0);
    color.w *= smoothstep(
        (1.0 - rayBrightnesses[RayIndex]) * rayLengths[RayIndex],
        (1.0 - rayBrightnesses[RayIndex] + 0.1) * rayLengths[RayIndex],
        projectedLength);
    FragColor = color;
}
