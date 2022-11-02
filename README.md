# cpython introspection

```py
New Documentation Tools: docs.py will help you automatically import and scan
all modules for '__docs__' (providing that none of them delete anything on import)
New Syntax: <<< and >>> to optionally replace python 'def' keyword
intended for running methods on other processors attached to the system

e.g.:

@random(ise = "<<<", r = ">>>")
<<<"Pi:80", x = ">>>", y = "<<<">>> X():
    nop
    print("<<<hello>>>")
    
becomes:

@random(ise = "<<<", r = ">>>")
def X():
    nop
    print("<<<hello>>>")
    
...or to put it more simply:

<<<"pi3">>> X():
    print("hello, world!")

The type of brackets could be changed (as yet untested):

["localhost:80"] X():
    print("hello, world!")

You can probably even point it to a Web URL:

["py://github.com/TheMindVirus/cuda/edge/runner:56789?a=1:b=2"]X():
    print("hello, world!")

The equivalent using decorators (I personally oppose this way of writing it):

@IRL(address = { "address": "localhost:12345" })
def X():
    calc = 2 + 2
    print(str(calc))
    return calc

Most of this was written on a phone! (apart from the actual cuda test implementation)
 
```

## Spherical Harmonics + Random Distortion = Grub Texture
![screenshot](https://github.com/TheMindVirus/cuda/blob/cpython/harmonicdistortion.png)
