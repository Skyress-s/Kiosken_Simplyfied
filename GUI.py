import tkinter as tk
import math
from main import *
from tkinter import filedialog, Text
import os

#defining som colors
backgroundColor = GetConfig(5)
foreground = GetConfig(6)
groupingColor = GetConfig(7)
GeneralButtonColor= GetConfig(4)
##6C698D
def ButtonAddItem(Entry = tk.Entry):
    input = Entry.get()
    input = str(input)
    input = input.split(',')
    appendItems(input[0], input[1])

    Entry.delete(0, 'end')

    # it has to append the item, but now we have add the button without reopening the program

def WriteToLabel():
    from main import items
    # experimental! not anymore! works like charm
    s = ""
    for item in items:
        if int(item[2]) != 0:
            string = str(item[0]) + " - " + str(item[2]) + "\n"
            s += string

    # adds the total price
    total = 0
    for x in range(0, len(items)):
        n = int(items[x][1]) * int(items[x][2])
        total += n

    s += '\n' + str(total)
    currentItems.config(text=s)


    currentItems.config(text=s)


root = tk.Tk()
root.title("Kiosken SIMPLIFIED") # adds the title


canvas = tk.Canvas(root, height=750, width=1100, bg=backgroundColor)
canvas.pack(fill="both", expand="true")

frame = tk.Frame(root, bg=foreground)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

# adds the frame and buttons for adding items

AdditemFrame = tk.Frame(frame, bg =groupingColor)

AdditemFrame.place(relx=0.97, rely=0.95,
                   height=70, width=150,
                   anchor="se")
#AdditemFrame.place(relx=0.8, rely = 0.8)


E1 = tk.Entry(AdditemFrame, bd = 2, width=20)
E1.pack(side="top")

AddNewItem = tk.Button(AdditemFrame, bd=0, text="Add New Item", padx=5, pady=5, fg="white", bg=GeneralButtonColor, command=lambda: ButtonAddItem(E1))
AddNewItem.pack(side="bottom")

# adds the button for saving to the log ;)

def NextCosOnClick():
    NextCostumer()
    WriteToLabel()
    DefualtToVipps()
#gets the button color for Next customer
nextcusCol = GetConfig(2);

BNextCostomer = tk.Button(frame, text="Next costumer", bd=0, width=20, height=3, fg="white", bg=nextcusCol,
                          command=lambda: NextCosOnClick())
#BNextCostomer.pack()
BNextCostomer.place(anchor="nw", relx=0.51, rely=0.03)
# adds tmp button for updating lable
#tmpButton = tk.Button(frame, text="updateLabel", width=10, height=3, fg="white", bg="#263D42", font="Helvetica")
#tmpButton.pack()

# adds the label for the current purchase

currentItems = tk.Label(frame, text="helwo,\n nå har du åpnet appen, \ndu trykker på items for å \nlegge dem til i handle" +
                        " \nkurven og \ntrykker på neste kunde\n for å legge det i loggen \n" +
                        " og til neste kunde, \n enjoy :)\n" +
                        "skriv in nye items \n på denne måten\n"+
                        "gjenstand,pris", width=25, height=30, fg="white", bg=groupingColor)
currentItems.place( anchor="s", rely=0.95, relx=0.5, relheight=0.8)

# adds the item buttons
for i in range(0, len(items)):
    padding = 10

    CollumLength = int(GetConfig(0))
    y = i % CollumLength
    x = math.floor(i/CollumLength)

    def shellfunc(tmp):  # updates the label AND makes the purchase
        purchase(tmp)
        WriteToLabel()


    item2 = tk.Button(frame, text=items[i][0], bd=0, width=12, height=2, fg="white", bg=GeneralButtonColor,
                      command=lambda tmp=i: shellfunc(tmp))
    # by using a temp value tmp, it will stay induvidual for each button :)
    item2.place(anchor="nw", x=x*100 + padding, y=y*50 + padding)


# adds the minus button
minusColor = "#E09891"
plussColor = "#BAD1CD"
def MinusShellFunc():
    global minusColor
    global plussColor

    ToggleMinusToggle()
    color = "magenta"
    b = GetMinusToggle()
    if b == False:
        color = minusColor
    else:
        color = plussColor
    BMinus.config(bg=color)


#BMinus = tk.Button(frame, text="toggleMinus", bd = 0, width=12, height=2, fg="white", bg=plussColor, command=lambda: MinusShellFunc())
#BMinus.place(anchor="ne", relx=0.97, rely=0.05)

def DefualtToVipps():
    SetToggleVippsBool(False)
    ToogleVippsShellFunc()


def ToogleVippsShellFunc():
    ToggleVippsBool()
    b = GetVippsBool()
    if b == False:
        BToggleVipps.config(text="Kontant")
        BToggleVipps.config(bg="#84CC76")
    else:
        BToggleVipps.config(text="Vipps")
        BToggleVipps.config(bg="#FF5B24")

BToggleVipps = tk.Button(frame, text="Vipps", bd=0, width=20, height=3, fg="white", bg="#FF5B24", command=lambda: ToogleVippsShellFunc())
BToggleVipps.place(anchor="ne", relx=0.49, rely=0.03)

# button clear current handlekurv

def ShellClearButton():
    clearCart()
    WriteToLabel()
#gets color for Clear button
clearButtonColor = GetConfig(3)
BClear = tk.Button(frame, text="Clear", bd=0, width=12, height=2, fg="white", bg=clearButtonColor, command=lambda: ShellClearButton())
BClear.place(anchor="e", relx=0.97, rely=0.5)


root.mainloop()
