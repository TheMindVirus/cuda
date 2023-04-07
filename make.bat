@echo off
set MSVC_PATH=%DevEnvDir%\..\..\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64
set PATH=%CUDA_PATH%;%MSVC_PATH%;%PATH%
nvcc main.cu -o app.exe
nvcc main.cu -o app.cubin -cubin
cuobjdump -h > cuobjdump.txt
nvdisasm -h > nvdisasm.txt
cuobjdump app.exe -sass -ptx > app.exe.txt
nvdisasm -hex app.cubin > app.cubin.txt
pause