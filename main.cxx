#include <stdio.h>
#include <Windows.h>

//#define import(FN) extern "C" { __declspec(dllimport) FN; }

//import(void load());

//typedef void(*load_t)();

int main()
{
    printf("[EDGE]: TPU\n");
    HMODULE mod = LoadLibrary("tpu.dll");
    if (!mod) { printf("[WARN]: Load Error\n"); return 1; }
    FARPROC load = GetProcAddress(mod, "load");
    if (load) { load(); } else { printf("[WARN]: Read Error\n"); return 1; }
    printf("[EDGE]: Done!\n");
    return 0;
}