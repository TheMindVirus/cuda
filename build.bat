@echo off
set GCC=%CD%/gxx-mingw32-msys64/usr/bin
set MSVC=%PROGRAMFILES(X86)%/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64
set MSVC_INC="%PROGRAMFILES(X86)%/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.29.30133/include"
set MSVC_LIB="%PROGRAMFILES(X86)%/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC/14.29.30133/lib/x64"
set UCRT_INC="%PROGRAMFILES(X86)%/Windows Kits/10/Include/10.0.19041.0/ucrt"
set UCRT_LIB="%PROGRAMFILES(X86)%/Windows Kits/10/Lib/10.0.19041.0/ucrt/x64"
set WINX_INC="%PROGRAMFILES(X86)%/Windows Kits/10/Include/10.0.19041.0/um"
set WINX_SINC="%PROGRAMFILES(X86)%/Windows Kits/10/Include/10.0.19041.0/shared"
set WINX_LIB="%PROGRAMFILES(X86)%/Windows Kits/10/Lib/10.0.19041.0/um/x64"
set TFLITE_INC="%CD%/tensorflow_1.15"
set TFLITE_SINC="%CD%/tensorflow_1.15/third_party/flatbuffers"
set CORAL_INC="%CD%/edgetpu_runtime_20221024/libedgetpu"
set CORAL_LIB="%CD%/edgetpu_runtime_20221024/libedgetpu/direct/x64_windows"
set PATH=%GCC%;%MSVC%;%PATH%
dir %CORAL_LIB%
g++.exe -v
rem g++.exe -c "tpu.cxx" -o "tpu.dll" 
cl.exe /I %MSVC_INC% /I %UCRT_INC% /I %WINX_INC% /I %WINX_SINC% ^
       /I %TFLITE_INC% /I %TFLITE_SINC% /I %CORAL_INC% ^
       /D_USRDLL /D_WINDLL "tpu.cxx" /link /LIBPATH:%MSVC_LIB% ^
       /LIBPATH:%UCRT_LIB% /LIBPATH:%WINX_LIB% /LIBPATH:%CORAL_LIB% "edgetpu.dll.if.lib" /DLL /OUT:"tpu.dll"
rem Rapid Eye Movement
g++.exe "main.cxx" -o "app.exe"
rem -L %CORAL_LIB% -l "edgetpu.dll.if.lib"
pause