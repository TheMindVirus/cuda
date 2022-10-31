@echo on
set PATH=%CD%\..\usr\bin;%PATH%
gcc.exe test.c -o test.c.exe
g++.exe test.cpp -o test.cpp.exe
cmd /K
pause