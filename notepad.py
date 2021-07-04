import os
# Import tkinter
from tkinter import*

root = Tk()
# title
root.title("Untitled - Notepad")
# Initial size of the program
root.geometry("640x480")
# User can resize the program
root.resizable(True, True)

# Frame
frame = Frame(root)
frame.pack()

# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Text Box
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text.yview)

# File name for save and open
filename = "mynote.txt"


# open file function
def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file: # open filename. reading function, with encoding utf-8
            text.delete("1.0", END) # Delete text widget information
            text.insert(END, file.read()) # Show output of text of the file
# save file function
def save_file():
    with open(filename, "w", encoding="utf8") as file: # save file, write function, with encoding utf-8
        file.write(text.get("1.0", END))

# menu user interface
menu = Menu(root)
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit", menu=menu_edit)

menu_format = Menu(menu,tearoff=0)
menu.add_cascade(label="Format", menu=menu_format)

menu_view = Menu(menu,tearoff=0)
menu.add_cascade(label="View", menu=menu_view)

menu_help = Menu(menu,tearoff=0)
menu.add_cascade(label="Help", menu=menu_help)



root.config(menu=menu)
root.mainloop()