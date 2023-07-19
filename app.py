from tkinter import ttk
from ttkthemes import ThemedTk

from GUI import GUI



# make sure to install required packages on requirements.txt

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    gui = GUI(root)
    root.mainloop()

