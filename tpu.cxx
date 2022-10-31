#include <stdio.h>
#include <Windows.h>
#include "edgetpu.h"

//#include "tensorflow/lite/interpreter.h"
//#include "tensorflow/lite/kernels/register.h"
//#include "tensorflow/lite/model.h"
//#include "tensorflow/lite/optional_debug_tools.h"

using namespace std;
//using namespace tflite;
//using namespace coral;
using namespace edgetpu;

#define export(FN) extern "C" { __declspec(dllexport) FN; }

export(void load());

void load()
{
    printf("[INFO]: OPEN_EDGE_TPU!\n");

    // Ask for EdgeTPU Manager
    auto manager = EdgeTpuManager::GetSingleton();

    // Enumerate Connected TPU Devices
    vector<EdgeTpuManager::DeviceEnumerationRecord> devices = manager->EnumerateEdgeTpu();
    for (int i = 0; i < devices.size(); ++i) { printf("[INFO]: %d: %s\n", i, devices[i].path.c_str()); }
    if (devices.size() == 0) { printf("[WARN]: No EdgeTPU Devices Detected\n"); }

    // Open First Available Device
    auto tpu_context = manager->OpenDevice();

    // Get a TPU Context
    tpu_context.get();

    // Reset the TPU Context
    tpu_context.reset();

    printf("[INFO]: CLOSE_EDGE_TPU!\n");
}