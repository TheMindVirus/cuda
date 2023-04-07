@echo off
set MSVC_PATH=%DevEnvDir%\..\..\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64
set PATH=%CUDA_PATH%;%MSVC_PATH%;%PATH%
cmd .