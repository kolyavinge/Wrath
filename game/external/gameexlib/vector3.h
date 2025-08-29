#pragma once

struct Vector3 {
    float x, y, z;
};

void addVectors(Vector3& v1, Vector3& v2, Vector3& result);
void subVectors(Vector3& v1, Vector3& v2, Vector3& result);
void mulVector(Vector3& v, float a);
void getMiddleBetweenVectors(Vector3& start, Vector3& end, Vector3& result);
float getLength(Vector3& v1, Vector3& v2);
float getDotProduct(Vector3& v1, Vector3& v2);
