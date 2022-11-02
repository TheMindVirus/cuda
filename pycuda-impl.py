#python3 -m pip install pycuda
#set PATH=%PATH%;%PROGRAMFILES(X86)%/Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64
#replace arbitrary directory with path to cl.exe in Visual Studio Build Tools
#WARNING: Be careful when using the set command to change the value of PATH!

import pycuda.autoinit
import pycuda.driver as GPU
import numpy as np

CUDA = \
"""
__global__ void mul(float* a, float* b, float* c)
{
    int i = threadIdx.x;
    c[i] = a[i] * b[i];
}
"""

from pycuda.compiler import SourceModule
code = SourceModule(CUDA)
mul = code.get_function("mul")

a = np.array((1.0, 2.0, 3.0), dtype = np.float32)
b = np.array((2.0, 3.0, 4.0), dtype = np.float32)
c = np.zeros_like(a)

mul(GPU.In(a), GPU.In(b), GPU.Out(c),
    block = (10, 1, 1), grid = (1, 1))
print(c)

"""
pycuda-impl.py:19: UserWarning: The CUDA compiler succeeded, but said the following:
kernel.cu

  code = SourceModule(CUDA)
[-0.46052846  1.7221541  -0.01192631 -0.5701643   0.2854798  -0.0475707
 -1.3542334  -0.11041633 -0.25468585 -0.42850178]
"""

"""
[ 2.  6. 12.]

"""
