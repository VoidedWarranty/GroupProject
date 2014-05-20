from Tkinter import Tk, Frame, Canvas
import ImageTk
import ctypes

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
root.bind("<Escape>", lambda e: e.widget.quit())

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=w, height=h)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="dungeonTile.jpg")
x = 0
y = 0
for i in range(f):
    for k in range(g):
        canvas.create_image(i*40, k*40, image=photoimage)

root.mainloop()
