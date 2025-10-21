#Imports
import tkinter as tk


#Turns it on, and the title of the window
root = tk.Tk()
title = root.title('tutorial_window')


#Text Label
message = tk.Label(root, text="Hello, World!")
message.pack()




#Window Height + Width
window_width = 300
window_height = 200

#Ur screen dimensions...
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Bullseye!
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#Hits the bullseye every dang time!
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#'parrently I need this
#Note to self: KEEP THIS AT THE END OF THE CODE, JESUS CHRIST YOU STUPIDO, NOTHING WILL WORK IF YOU DON'T!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
root.mainloop()