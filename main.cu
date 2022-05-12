#include <stdio.h>
#include <stdarg.h>
#include <cuda_runtime.h>

#define GPU __global__

#define GPU_DATA(TYPE, NAME, VALUE)   \
    TYPE* NAME;                        \
    NAME = (TYPE*)malloc(sizeof(TYPE)); \
    *NAME = (TYPE)VALUE;                 \
    TYPE* gpu_##NAME;                     \
    cudaMalloc((void**)&gpu_##NAME, sizeof(TYPE));

#define GPU_DATA_N(TYPE, NAME, SIZE, VALUE)                    \
    TYPE* NAME;                                                 \
    NAME = (TYPE*)malloc(sizeof(TYPE) * SIZE));                  \
    { for (int i = 0; i < SIZE; ++i) { NAME[i] = (TYPE)VALUE; } } \
    TYPE* gpu_##NAME;                                              \
    cudaMalloc((void**)&gpu_##NAME, sizeof(TYPE) * SIZE);           \
    
#define GPU_SEND(TYPE, NAME)           cudaMemcpy(gpu_##NAME, NAME, sizeof(TYPE), cudaMemcpyHostToDevice);
#define GPU_SEND_N(TYPE, NAME, SIZE)   cudaMemcpy(gpu_##NAME, NAME, sizeof(TYPE) * SIZE, cudaMemcpyHostToDevice);

#define GPU_SYNC(TYPE, NAME)           cudaMemcpy(NAME, gpu_##NAME, sizeof(TYPE), cudaMemcpyDeviceToHost);
#define GPU_SYNC_N(TYPE, NAME, SIZE)   cudaMemcpy(NAME, gpu_##NAME, sizeof(TYPE) * SIZE, cudaMemcpyDeviceToHost);

#define GPU_CALL(METHOD, ...)                    METHOD<<<1, 1>>>(__VA_ARGS__)
#define GPU_CALL_G_B(METHOD, GRID, BLOCK, ...)   METHOD<GRID, BLOCK>(__VA_ARGS__)

#define GPU_FREE(NAME) free(NAME); cudaFree(gpu_##NAME);

GPU void cuda(float* a, float* b, float* c)
{
    printf("[CUDA]: Begin: %f + %f\n", *a, *b);
    //*c = *a + *b;
    asm("add.f32 %0,%1,%2;" : "=f"(*c) : "f"(*a), "f"(*b));
    printf("[CUDA]: End: %f\n", *c);
}

void delay(clock_t i)
{
    clock_t t1 = clock();
    clock_t t2 = 0;
    while (t2 < t1 + i) { t2 = clock(); }
}

int main()
{
    GPU_DATA(float, a, 1);
    GPU_DATA(float, b, 2); 
    GPU_DATA(float, c, 0);
    GPU_SEND(float, a);
    GPU_SEND(float, b);
    GPU_CALL(cuda, gpu_a, gpu_b, gpu_c);
    while (*c == 0.0f)
    {
        GPU_SYNC(float, c);
        printf("[INFO]: PTX-TEST: %f + %f = %f\n", *a, *b, *c);
        delay(1000);
    }
    GPU_FREE(a);
    GPU_FREE(b);
    GPU_FREE(c);
    return 0;
}

#define GPU_SLI(TYPE, SRC, DST)           cudaMemcpy(DST, SRC, sizeof(TYPE), cudaMemcpyDeviceToDevice);
#define GPU_SLI_N(TYPE, SRC, DST, SIZE)   cudaMemcpy(DST, SRC, sizeof(TYPE) * SIZE, cudaMemcpyDeviceToDevice);

#define CPU_SLI(TYPE, SRC, DST)           cudaMemcpy(DST, SRC, sizeof(TYPE), cudaMemcpyHostToHost);
#define CPU_SLI_N(TYPE, SRC, DST, SIZE)   cudaMemcpy(DST, SRC, sizeof(TYPE) * SIZE, cudaMemcpyHostToHost);