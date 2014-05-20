from Tkinter import Tk, Frame, Canvas
import ImageTk
import ctypes
import Image
import sys

def quitapp(event):
    root.destroy()

user32 = ctypes.windll.user32
w = int(user32.GetSystemMetrics(0))
h = int(user32.GetSystemMetrics(1))
f = int(w/40)
g = int(h/40)

print w

root = Tk()
root.title("Transparency")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
print w, h
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", quitapp)

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=w, height=h)
canvas.pack()

photoimage = ImageTk.PhotoImage(Image.open("dungeonTile.jpg"))
x = 0
y = 0
for i in range(f+1):
    for k in range(g+1):
        canvas.create_image(i*40, k*40, image=photoimage)

root.mainloop()
