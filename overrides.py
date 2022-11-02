c = 'print(x)\nx+=1'

def wrap(code, x):
    exec(compile(code, "wrap", "exec"))
    return x

n = lambda x: wrap(c, x)
print(n(5))

def override(__code__, this, \
    *__register__, **__registry__):
    print(this)
    for reg in __register__:
        print(reg)
    for key in __registry__:
        print(key, __registry__[key])
        exec("{}={}".format(key, \
            __registry__[key]))
    exec(compile(__code__, \
        "<string>", "exec"))
    return __result__

A = 'global __result__; \
    __result__ = x + 1'
B = type("B", (object,), \
    {"A": lambda self, *args, **kwargs: \
    override(A, self, *args, **kwargs)})
C = B().A(0, z = 1, x = 2)
print(C)

# Just don't use decorators.
# If you really need to use them,
# try overriding the def keyword instead.
# Also try swapping out def override()
# for one that exec's on a remote system.

"""
5
5
<__main__.B object at 0x0000018CFD382070>
0
z 1
x 2
3
>>>
"""
