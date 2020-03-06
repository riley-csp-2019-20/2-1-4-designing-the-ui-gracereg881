import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

# blue screen
blue = tk.Frame(root)
blue.grid(row = 0, column = 0)
blue.config(bg = "blue", height = "100", width = "125")

# green screen 
green = tk.Frame(root)
green.grid(row = 0, column = 1)
green.config(bg = "lime", height = "100", width = "75")


# yellow screen
yellow = tk.Frame(root)
yellow.grid(row = 1, column = 1)
yellow.config(bg = "yellow", height = "100", width = "75")


# red screen
red = tk.Frame(root)
red.grid(row = 1, column = 0)
red.config(bg = "red", height = "100", width = "125")


root.mainloop()