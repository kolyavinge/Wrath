#include "pch.h"
#include <math.h>
#include "vector3.h"

void addVectors(Vector3& v1, Vector3& v2, Vector3& result) {
    result.x = v2.x + v1.x;
    result.y = v2.y + v1.y;
    result.z = v2.z + v1.z;
}

void subVectors(Vector3& v1, Vector3& v2, Vector3& result) {
    result.x = v1.x - v2.x;
    result.y = v1.y - v2.y;
    result.z = v1.z - v2.z;
}

void mulVector(Vector3& v, float a) {
    v.x *= a;
    v.y *= a;
    v.z *= a;
}

void getMiddleBetweenVectors(Vector3& start, Vector3& end, Vector3& result) {
    subVectors(end, start, result);
    mulVector(result, 0.5f);
    addVectors(result, start, result);
}

float getLength(Vector3& v1, Vector3& v2) {
    float x = v2.x - v1.x;
    float y = v2.y - v1.y;
    float z = v2.z - v1.z;

    return sqrtf(x * x + y * y + z * z);
}

float getDotProduct(Vector3& v1, Vector3& v2) {
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z);
}
