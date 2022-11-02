method = \
"""
@random(ise = "<<<", r = ">>>")
<<<"Pi:80", x = ">>>", y = "<<<">>> X():
    nop
    print("<<<hello>>>")
"""

def bracket(x, o = "<<<", c = ">>>"):
    inside = None
    xl = len(x)
    ol = len(o)
    cl = len(c)
    ai = 0
    for i in range(0, xl):
        a = method.find(o, ai)
        if a < 0:
            break
        ai = a + ol
        bi = i
        for j in range(i, xl):
            b = method.find(c, bi)
            #print(i, j, a, b)
            if b < 0:
                break
            bi = b + ol + cl
            tok = o + method[a + ol:b] + c
            try:
                test = method.replace( \
                    tok, "def")
                #print(test)
                compile(test, "", "exec")
                #print("compiles")
                inside = tok
            except Exception as error:
                #print(error)
                pass
    return inside

inside = bracket(method)
print(inside)
if "Pi" in inside.split(",")[0]:
    pi_code = method.replace(inside, "def")
    print("[PiCode]")
    print(pi_code)

"""
<<<"Pi:80", x = ">>>", y = "<<<">>>
[PiCode]

@random(ise = "<<<", r = ">>>")
def X():
    nop
    print("<<<hello>>>")

>>>
"""