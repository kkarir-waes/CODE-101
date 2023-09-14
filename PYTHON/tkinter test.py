from tkinter import *
from tkinter import ttk


# instantiate a Tk root window
root_window = Tk()


# set up a frame within the root window
window_frame = ttk.Frame(root_window, padding=10)
window_frame.grid()

# create ttk widgets - a label & and button
ttk.Label(window_frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(window_frame, text="Quit", command=root_window.destroy).grid(column=1, row=0)


root_window.mainloop()
