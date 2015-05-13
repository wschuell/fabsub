import Tkinter
import subprocess
import os
import evince

main = Tkinter.Tk()

def page():
	return 

def leftKey(event):
    subprocess.call("ls")

def rightKey(event):
    print "Right key pressed"
    i=0

def upKey(event):
    subprocess.call("ls")
    os.system("evince subtitles_beamer.pdf --page-label=5")#+str(5))
    print i

def downtKey(event):
    print "Down key pressed"

frame = Tkinter.Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Down>', downtKey)
#frame.pack()
main.mainloop()