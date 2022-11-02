#import ast
import inspect

#rp2 = def # This doesn't work normally

def replace_code(code):
    tokens = code.split("\"")

code = \
"""
def.rp2 something(data):
    print("[INFO]: " + str(data) + " [def.rp2]")
"""

code = code.replace("def.rp2", "@rp2statemachineblablabla\ndef")
print(code)

#asm = ast.parse(code)
#dis = ast.unparse(asm)
#print(ast.dump(asm))
#print(dis)

code = code.replace("@rp2statemachineblablabla\ndef", "def")
exec(code)
something("RP2")

"""
@rp2statemachineblablabla
def something(data):
    print("[INFO]: " + str(data) + " [@rp2statemachineblablabla
def]")

[INFO]: RP2 [def]
"""

class Storage:
    pass

Storage()
print(__name__)

def \
Method(*args):
    #Method.hello()
    def \
        hello():
        print(hello.__name__ + str(args))
    hello()
    print(Method.__name__ + str(args))
    if len(args) > 0:
        print(args[0].__class__()) # missing code?
    #return None #args[0] # This is how deprecation functions.
    return None

Method()

class Template:
    @Method
    def \
        __init__(self, *args):
        calls = ""
        stack = inspect.stack()
        for i in range(len(stack) -1, -1, -1):
            calls += stack[i].function
            if i > 0:
                calls += " -> "
        print(calls)
        print(self.__init__.__qualname__ + str(args))
        #Any way to get self.__init__ dynamically?
        #Especially for full stack traces like WinDbg for Windows
Template()

"""

@rp2statemachineblablabla
def something(data):
    print("[INFO]: " + str(data) + " [@rp2statemachineblablabla
def]")

[INFO]: RP2 [def]
__main__
hello()
Method()
hello(<function Template.__init__ at 0x0000019EAD0BE830>,)
Method(<function Template.__init__ at 0x0000019EAD0BE830>,)
Traceback (most recent call last):
  File "[REDACTED]" line 57, in <module>
    class Template:
  File "[REDACTED]", line 59, in Template
    def \
  File "[REDACTED]", line 51, in Method
    print(args[0].__class__()) # missing code?
TypeError: function() missing required argument 'code' (pos 1)
"""
