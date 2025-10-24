#Imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

#Turns it on, and the title of the window
root = tk.Tk()
title = root.title('tutorial_window')

def new_window():
    pass

class NewWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("New Window")
        self.geometry("250x150")

        Label(self, text="This is a new window").pack(pady=20)

#Buttons!
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

page1_button = ttk.Button(
    root,
    text='Page_1',
    command=new_window()
)

#Labels!
tk.Label(root, text='This is an older label').pack()

ttk.Label(root, text='This is a newer,themed label!').pack()

#Text Label
message = tk.Label(root, text="Hello, World!")
message.pack()


#puts the button in a specific spot
exit_button.place(x=100, y=20)
page1_button.place(x=0, y=20)

#Window Height + Width
window_width = 300
window_height = 200

#Ur screen dimensions...
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Bullseye!
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#Makes it big
root.geometry('1000x1000')

#Tranparency of window
root.attributes('-alpha', 0.9)


#'parrently I need this
#Note to self: KEEP THIS AT THE END OF THE CODE, JESUS CHRIST YOU STUPIDO, NOTHING WILL WORK IF YOU DON'T!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
root.mainloop()