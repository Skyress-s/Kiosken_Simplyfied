import tkinter as tk
import math
from main2 import *

#defining som colors
backgroundColor = GetConfig(5)
foreground = GetConfig(6)
groupingColor = GetConfig(7)
GeneralButtonColor= GetConfig(4)


root = tk.Tk()
root.title("Kiosken SIMPLIFIED") # adds the title


canvas = tk.Canvas(root, height=750, width=1100, bg=backgroundColor)
canvas.pack(fill="both", expand="true")


root.mainloop()