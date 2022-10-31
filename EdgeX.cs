using UnityEngine;
using System.Runtime.InteropServices;

public class EdgeX : MonoBehaviour
{
    [DllImport("tpu.dll")] private static extern void load();

    void Start() { try { load(); } catch { Debug.Log("Error"); } }

    void Update() { }
}
