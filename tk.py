import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import os
import distance_from_camera


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "C:\\Users\\SourAv\\Desktop\\Mtech\\oose lab",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.jpg*"),
                                                       ("all files",
                                                        "*.*")))
    filename=os.path.relpath(filename,"C:\\Users\\SourAv\\Desktop\\Mtech\\oose lab")
    label_file_opend.configure(text="File Opened: "+filename)
    value = distance_from_camera.distance_main(filename)
    label_value.configure(text="Distance="+str("{:.2f}".format(value*2.54))+"cm")

      

window = tkinter.Tk()
  
# Set window title
window.title('APP')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Distance Measure App",
                            width = 100, height = 4,
                            fg = "blue")
label_file_opend = Label(window,
                            text = "File ",
                            width = 100, height = 4,
                            fg = "blue")
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)

label_value = Label(window,
                            text = "Distance",
                            width = 100, height = 4,
                            fg = "blue")
  
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1,sticky='')
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
label_file_opend.grid(column = 1,row = 4)
label_value.grid(column=1,row=5)  
# Let the window wait for any events
window.mainloop()

B = tkinter.Button(top, text ="Select image", command = browseFiles)

B.pack()
top.mainloop()