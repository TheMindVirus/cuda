using UnityEngine;
using System;
using System.Runtime;
using System.Runtime.InteropServices;
using System.IO.Ports;
using System.Text;

public class EdgeX : MonoBehaviour
{
    [DllImport("tpu.dll")] private static extern void load();

    void Start() { try { load(); } catch { Debug.Log("Error"); } StartEdgeX("Hello World!", "COM6", 115200); }

    //void Update() { Debug.Log("[XCOM]: " + XCOM.BytesToRead.ToString()); } //C# Serial Ports are Rigged with Semaphores...

    static SerialPort XCOM = null;
    static string CodeX = "";
    static string _tmp = "";

    void OnDestroy() { if (XCOM != null) { XCOM.Close(); XCOM = null; } }

    void StartEdgeX(string data, string port, int baud = 115200)
    {
        Debug.Log("[INFO]: StartEdgeX");
        if (XCOM == null)
        {
            XCOM = new SerialPort(); //CXL???
            XCOM.PortName = port;
            XCOM.BaudRate = baud;
            XCOM.DataBits = 8;
            XCOM.Parity = Parity.None;
            XCOM.StopBits = StopBits.One;

            XCOM.NewLine = "\r\n";
            XCOM.RtsEnable = true;
            XCOM.ReadTimeout = 10000;
            XCOM.WriteTimeout = 10000;
            XCOM.ReadBufferSize = 4096;
            XCOM.WriteBufferSize = 2048;

            XCOM.ParityReplace = 0;
            XCOM.DiscardNull = true;
            XCOM.DtrEnable = true;
            XCOM.Encoding = new ASCIIEncoding(); //new UTF32Encoding();
            XCOM.Handshake = Handshake.XOnXOff; //These options were rigged externally

            XCOM.DataReceived += UpdateEdgeX;
            XCOM.ErrorReceived += ErrorEdgeX;
            XCOM.Open();
        }
        XCOM.Read(new byte[XCOM.BytesToRead], 0, XCOM.BytesToRead); //Flush
        XCOM.WriteLine(data);
    }

    private static void UpdateEdgeX(object xcom, SerialDataReceivedEventArgs evt)
    {
        SerialPort dev = (SerialPort)xcom;
        for (int i = 0; i < XCOM.BytesToRead; ++i)
        {
            char c = (char)dev.ReadByte();
            if (c == '\n') { CodeX = _tmp; Debug.Log("[XCOM]: " + CodeX); _tmp = ""; } //Subject to Change without Notice...
            else if (((int)c >= 32) && ((int)c < 127)) { _tmp += c; }
        }
    }

    private static void ErrorEdgeX(object xcom, SerialErrorReceivedEventArgs evt)
    {
        Debug.Log("[WARN]: XCOM");
    }
}