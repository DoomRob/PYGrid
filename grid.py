from tkinter import *

root = Tk()

# Create Label Widget
label1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
label2 = Label(root, text = "My Name is Robert").grid(row = 1, column = 1)
# Displays the text on screen
# label1.grid(row = 0, column = 0)
# label2.grid(row = 1, column = 1)

# Execution
root.mainloop()
