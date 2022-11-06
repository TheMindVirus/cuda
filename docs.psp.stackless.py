import sys, psp2d

controls = \
{
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
    "cross": 0,
    "circle": 0,
    "square": 0,
    "triangle": 0,
    "l": 0,
    "r": 0,
    "start": 0,
    "select": 0,
    "analogX": 0,
    "analogY": 0,
}

w = 480
h = 272
font = psp2d.Font("font.png")
image = psp2d.Image(w, h)
screen = psp2d.Screen()
blank = psp2d.Color(0, 0, 0)
origin = 0

def blank_screen(r = 30, g = 0, b = 255):
    global screen, blank
    blank = psp2d.Color(r, g, b)
    image.clear(blank)
    screen.blit(image)
    screen.swap()

def draw_text(message):
    global origin, image, screen
    font.drawText(image, 0, origin, "[INFO]: " + message)
    screen.blit(image)
    screen.swap()
    origin += 30

def update_controls():
    pad = psp2d.Controller()
    for control in controls.keys():
        controls[control] = getattr(pad, control)

def reset_file(filename, data, sure = "No"):
    if (sure == "Sure"):
        file = open(filename, "w")
        file.write(data)
        file.close()

def write_file(filename, data):
    file = open(filename, "a")
    file.write(data)
    file.close()

def read_file(filename):
    data = ""
    file = open(filename, "r")
    data = file.read()
    file.close()
    return data

def blank():
    blank_screen()

def log(*args):
    for arg in args:
        write_file("log.txt", str(arg) + "\n")
reset_file("log.txt", "", "Sure")

def show(*args):
    for arg in args:
        draw_text(str(arg))
#overriding print doesn't work on stackless

def logshow(*args):
    log(args)
    show(args)

#from lib_tk import Tkinter
#app = tk.Tk()
#__import__("lib-tk.Tkinter")
#if Tkinter:
#    show("Tkinter Found")
#Tkinter is not configured correctly for stackless

running = True #False # Whether or not to crash on error

def main():
    global running
    try:
        setup()
        running = True
        update_controls()
        #raise Exception("hello")
    #except Exception as error:
    except Exception, error: #Stackless is Python2.5
        logshow(error)

    while running:
        try:
            update_controls()
            if loop() == 0:
                running = False
        except Exception, error:
            logshow(error)

def setup():
    blank()
    show("Hello World")
    show("Press X to Exit")
    log(sys.version)
    log("[TEST]")
    show(read_file("log.txt"))
    log(sys.modules)

    for mod in sys.modules.keys():
        try:
            try:
                exec("import " + mod)
                exec('logshow("' + mod + ': " + str(dir(' + mod + ')))')
            except:
                alias = mod.replace(".", "_")
                tree = mod.split(".")
                name = tree.pop()
                tree = "".join(tree)
                exec("from " + tree + " import " + name + " as " + alias)
                exec('logshow("' + mod + ': " + str(dir(' + alias + ')))')
        except Exception, error:
            logshow(error)

def loop():
    if controls["circle"]:
        show("Restarting...")
        return 0

if __name__ == "__main__":
    main()