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

frame = tk.Frame(root, bg=foreground)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

label1 = tk.Label(frame, text="hello")
label1.grid(row=0, column=4, padx = 10, pady = 10)

label2 = tk.Label(frame, text="hello")
label2.grid(row=0, column=5, padx = 10, pady = 10)







#creates the item buttons
for i in range(0, len(items)):
    padding = 10

    CollumLength = int(GetConfig(0))
    y = i % CollumLength
    x = math.floor(i/CollumLength)

    #def shellfunc(tmp):  # updates the label AND makes the purchase
       # purchase(tmp)
       # WriteToLabel()


    item2 = tk.Button(frame, text=items[i][0], bd=0, width=12, height=2, fg="white", bg=GeneralButtonColor,
                      command=lambda tmp=i: #shellfunc(tmp))
    # by using a temp value tmp, it will stay induvidual for each button :)
    item2.place(anchor="nw", x=x*100 + padding, y=y*50 + padding)




root.mainloop()