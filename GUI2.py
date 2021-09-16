import tkinter as tk
import math
from main2 import *

#defining som colors
backgroundColor = GetConfig(5)
foreground = GetConfig(6)
groupingColor = GetConfig(7)
GeneralButtonColor= GetConfig(4)

#----------------
LoadItemsFromData()

#--------------


root = tk.Tk()
root.title("Kiosken SIMPLIFIED") # adds the title


canvas = tk.Canvas(root, height=750, width=1300, bg=backgroundColor)
canvas.pack(fill="both", expand="true")

frame = tk.Frame(root, bg=foreground)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


def PlaceAddNewItenButton():
    AdditemFrame = tk.Frame(frame, bg=groupingColor)

    AdditemFrame.place(relx=0.97, rely=0.95,
                       height=70, width=150,
                       anchor="se")

    E1 = tk.Entry(AdditemFrame, bd=2, width=20)
    E1.pack(side="top")


    def OnAddNewItemClick(Entry = tk.Entry):
        input = Entry.get()
        input = str(input)
        input = input.split(',')
        AddNewItemToItemsFile(input[0], input[1])

        Entry.delete(0, 'end')

    AddNewItem = tk.Button(AdditemFrame, bd=0, text="Add New Item", padx=5, pady=5, fg="white", bg=GeneralButtonColor, command=lambda: OnAddNewItemClick(E1))
    AddNewItem.pack(side="bottom")

PlaceAddNewItenButton()

def PlaceItemButtons():
    def placeholder(num = 0):
        AddToCart(num)
        WriteToCurrentItemsView()

    items = LoadItemsFromData()

    #creates the item buttons
    for i in range(0, len(items)):
        allItems = LoadItemsFromData()
        # the logic for placing the buttons
        padding = 10

        CollumLength = int(GetConfig(0))
        y = i % CollumLength
        x = math.floor(i/CollumLength)


        # loads the items from the txt file


        item2 = tk.Button(frame, text=allItems[i][0], bd=0, width=12, height=2, fg="white", bg=GeneralButtonColor,
                          command=lambda tmp=i: placeholder(tmp))

        # by using a temp value tmp, it will stay induvidual for each button :)
        item2.place(anchor="nw", x=x*100 + padding, y=y*50 + padding)

PlaceItemButtons()


#def CurrentItemsView():
# current items
currentItems = tk.Label(frame, text="helwo,\n nå har du åpnet appen, \ndu trykker på items for å \nlegge dem til i handle" +
                        " \nkurven og \ntrykker på neste kunde\n for å legge det i loggen \n" +
                        " og til neste kunde, \n enjoy :)\n" +
                        "skriv in nye items \n på denne måten\n"+
                        "gjenstand,pris", width=25, height=30, fg="white", bg=groupingColor)
currentItems.place( anchor="s", rely=0.95, relx=0.5, relheight=0.8)
#CurrentItemsView()

def WriteToCurrentItemsView():
    items = LoadItemsFromData()
    cart = GetCurrentCart()
    s = ""
    # prints all the items and the amount of them
    for i in range(0,len(items)):
        if cart[i] > 0:
            s += items[i][0] + " - "
            s += str(cart[i])
            s += '\n'

    #adds the sum of all current items thus far
    s += '\n'
    price = 0
    for i in range(0, len(items)):
        price += cart[i] * items[i][1]

    s += str(price)


    currentItems.config(text=s)


def PaymentMethodButton():

    def OnClick(button = tk.Button):
        if  GetCurrentPaymentMethod() == PaymentMethod.Vipps:
            SetCurrentPaymentMethod(PaymentMethod.Kontant)
            button.config(text = "Kontant")
            button.config(bg=GetConfig(10))

        elif GetCurrentPaymentMethod() == PaymentMethod.Kontant:
            SetCurrentPaymentMethod(PaymentMethod.Kort)
            button.config(text = "Kort")
            button.config(bg=GetConfig(11))

        elif GetCurrentPaymentMethod() == PaymentMethod.Kort:
            SetCurrentPaymentMethod(PaymentMethod.Vipps)
            button.config(text = "Vipps")
            button.config(bg=GetConfig(9))



    BToggleVipps = tk.Button(frame, text="Vipps", bd=0, width=20, height=3, fg="white", bg=GetConfig(9),
                             command=lambda: OnClick(BToggleVipps))
    BToggleVipps.place(anchor="ne", relx=0.49, rely=0.03)
PaymentMethodButton()


def ClearCartButton():

    def OnClick():
        InitAndResetCart()
        WriteToCurrentItemsView()

    clearButtonColor = GetConfig(3)
    BClear = tk.Button(frame, text="Clear", bd=0, width=12, height=2, fg="white", bg=clearButtonColor,
                       command=lambda: OnClick())
    BClear.place(anchor="e", relx=0.97, rely=0.5)
ClearCartButton()


def PlaceNextCustomerutton():

    def OnClick():
        t =1
    BNextCostomer = tk.Button(frame, text="Next costumer", bd=0, width=20, height=3, fg="white", bg=GetConfig(2),
                              command=lambda: OnClick())
    #BNextCostomer.pack()
    BNextCostomer.place(anchor="nw", relx=0.51, rely=0.03)
PlaceNextCustomerutton()




root.mainloop()