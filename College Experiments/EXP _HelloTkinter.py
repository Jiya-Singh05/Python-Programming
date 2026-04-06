#Create a simple Tkinter window with a title and fixed size

import tkinter as tk
root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("400x300")
root.resizable(False, False)
root.mainloop()
