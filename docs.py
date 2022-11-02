import sys

def man(mods):
    for mod in mods:
        sys.stdout.write("[{}".format(mod))
        try:
            exec("import " + mod)
        except:
            sys.stdout.write("(nested)")
            sys.stdout.write("]\n['']\n\n")
            continue
        sys.stdout.write("]\n")
        try:
            exec('print(dir(' + mod + '))')
        except:
            print('[]')
        sys.stdout.write("\n")
        try:
            exec('print(' \
            + mod + '.__doc__)')
        except:
            print("None")
        sys.stdout.write("\n")

man(sys.builtin_module_names)
man(sys.modules)