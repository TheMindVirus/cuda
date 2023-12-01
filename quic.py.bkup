#Sipeed MaixPy MicroPython v0.6.2-84-g8fcd84a58 on 2022-08-26; Sipeed_M1 with kendryte-k210
from Maix import GPIO
from fpioa_manager import fm
from machine import Timer
import random

PIN_R = 9
PIN_V = 33
PIN_G = 11
PIN_B = 14

fm.fpioa.set_function(PIN_R, fm.fpioa.GPIO1)
fm.fpioa.set_function(PIN_V, fm.fpioa.GPIO2)
fm.fpioa.set_function(PIN_G, fm.fpioa.GPIO3)
fm.fpioa.set_function(PIN_B, fm.fpioa.GPIO4)

red   = GPIO(GPIO.GPIO1, GPIO.OUT)
vgnd  = GPIO(GPIO.GPIO2, GPIO.OUT)
green = GPIO(GPIO.GPIO3, GPIO.OUT)
blue  = GPIO(GPIO.GPIO4, GPIO.OUT)

red.value(1 - (0))
vgnd.value(1 - (0))
green.value(1 - (0))
blue.value(1 - (0))

quic_server_messages = \
[
"QUIC_STREAM_EVENT_SEND_COMPLETE",
"QUIC_STREAM_EVENT_RECEIVE",
"QUIC_STREAM_EVENT_PEER_SEND_SHUTDOWN",
"QUIC_STREAM_EVENT_PEER_SEND_ABORTED",
"QUIC_STREAM_EVENT_SHUTDOWN_COMPLETE",

"QUIC_CONNECTION_EVENT_CONNECTED",
"QUIC_CONNECTION_EVENT_SHUTDOWN_INITIATED_BY_TRANSPORT",
"QUIC_CONNECTION_EVENT_SHUTDOWN_INITIATED_BY_PEER",
"QUIC_CONNECTION_EVENT_SHUTDOWN_COMPLETE",
"QUIC_CONNECTION_EVENT_PEER_STREAM_STARTED",
"QUIC_CONNECTION_EVENT_RESUMED",

"QUIC_LISTENER_EVENT_NEW_CONNECTION",
]

quic_client_messages = \
[
"QUIC_STREAM_EVENT_SEND_COMPLETE",
"QUIC_STREAM_EVENT_RECEIVE",
"QUIC_STREAM_EVENT_PEER_SEND_ABORTED",
"QUIC_STREAM_EVENT_PEER_SEND_SHUTDOWN",
"QUIC_STREAM_EVENT_SHUTDOWN_COMPLETE",

"QUIC_CONNECTION_EVENT_CONNECTED",
"QUIC_CONNECTION_EVENT_SHUTDOWN_INITIATED_BY_TRANSPORT",
"QUIC_CONNECTION_EVENT_SHUTDOWN_INITIATED_BY_PEER",
"QUIC_CONNECTION_EVENT_SHUTDOWN_COMPLETE",
"QUIC_CONNECTION_EVENT_RESUMPTION_TICKET_RECEIVED",
]

class control:
    def __init__(self, name = "CONTROL", messages = ["BLIP"]):
        self.name = name
        self.msgid = 0
        self.messages = messages
        self.message = self.messages[self.msgid]
        self.kernel = None
        self.kernel_timesrc = Timer.TIMER1
        self.kernel_channel = Timer.CHANNEL0
        self.module = None
        self.module_timesrc = Timer.TIMER2
        self.module_channel = Timer.CHANNEL1
        self.errors = None
    def start(self):
        self.kernel = Timer(self.kernel_timesrc, self.kernel_channel, mode = Timer.MODE_PERIODIC,
            period = self.new_interval(), unit = Timer.UNIT_MS, callback = self.run, start = True, priority = 1)
    def stop(self):
        self.kernel.stop()
    def run(self, sender):
        self.new_message()
        print("[INFO]:", str(self.name) + ":", self.message)
        try:
            self.mod(self.msgid, self.message, self.name)
        except Exception as error:
            self.errors = error
            print("[WARN]:", str(self.name) + ":", self.errors)
            self.kernel.period(1)
        finally:
            self.kernel.period(self.new_interval())
    def new_message(self):
        self.msgid = random.randint(0, len(self.messages) - 1)
        self.message = self.messages[self.msgid]
    def new_interval(self, minimum = 100, maximum = 3000):
        return int(min(max(random.random() * maximum, minimum), maximum))
    def mod(self, msgid, message, name):
        global red, blue
        self.blink(red if name == "QUIC_SERVER" else blue, 10 + msgid)
    def blink(self, LED, duration = 10):
        LED.value(1 - (1))
        def module_callback(_):
            LED.value(1 - (0))
        self.module = Timer(self.module_timesrc, self.module_channel, mode = Timer.MODE_ONE_SHOT,
            period = duration, unit = Timer.UNIT_MS, callback = module_callback, start = True, priority = 2)

server = control("QUIC_SERVER", quic_server_messages)
client = control("QUIC_CLIENT", quic_client_messages)

server.kernel_timesrc = Timer.TIMER0
server.kernel_channel = Timer.CHANNEL0
server.module_timesrc = Timer.TIMER2
server.module_channel = Timer.CHANNEL2

client.kernel_timesrc = Timer.TIMER1
client.kernel_channel = Timer.CHANNEL1
client.module_timesrc = Timer.TIMER2
client.module_channel = Timer.CHANNEL3

#import quic
#quic.server.start()
#quic.client.start()
#quic.server.stop()
#quic.client.stop()

def start():
    server.start()
    client.start()

def stop():
    server.stop()
    client.stop()