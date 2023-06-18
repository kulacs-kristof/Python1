# Create an app with tkinter
from tkinter import *


# Create an instance
win = Tk()

# Add a title
win.title("Python GUI")

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)

# Make the GUI stay on top of other windows at all times
win.wm_attributes("-topmost", 1)

# Make a slider that stores its value in a variable
slider = Scale(win, from_=20, to=100, orient=HORIZONTAL, length=300)
slider.pack()
slider.set(100)

# Call a function when the slider is moved
slider.bind("<ButtonRelease-1>", lambda event: transparency())

# Make the transparency of the window equal to the slider's value


def transparency():
    win.attributes("-alpha", slider.get() / 100)


# Start GUI
win.mainloop()
