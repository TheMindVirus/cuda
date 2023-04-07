#include <stdio.h>
#include <cuda.h>

__global__ void VecAdd(float* A, float* B, float* C)
{
    int i = threadIdx.x;
    C[i] = A[i] + B[i];
}

int main()
{
    printf("[INFO]: %s\n", "TEST");
    double a = acos(1);
    float A = 1;
    float B = 2;
    float C = 0;
    int K = 1;
    int N = 10;
    VecAdd<<<K, N>>>(&A, &B, &C);
    return 0;
}