def method(*args, **kwargs):
    print(args, kwargs)
    return args[0] if len(args) else method

class test1:
    @method
    def __init__(self, *args):
        print(args)

class test2:
    @method(something = 1)
    def test3(self):
        print("hello")

A = method
B = type("B", (object,), {"A": A})
C = B().A(0, z = 1, x = 2)
print(C)

test1()
a = test2()
a.test3()

# Decorators cause 2 very bad things:
# 1) Deprecation - missing implementations
# 2) Complexity - things that don't compile

"""
(<function test1.__init__ at 0x0000021CD6A2E9D0>,) {}
() {'something': 1}
(<function test2.test3 at 0x0000021CD6A2EA60>,) {}
(<__main__.B object at 0x0000021CD6A32970>, 0) {'z': 1, 'x': 2}
<__main__.B object at 0x0000021CD6A32970>
()
hello
>>>
"""
