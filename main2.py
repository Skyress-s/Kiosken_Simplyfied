from datetime import datetime
import os
from enum import Enum
# all global items are defined here
ItemsPath = 'Items.txt'

currentCart = [] # has this form currentcart[index][currentPaymentMethod] ie. index 0 = solo 1 = pepsi, cPM it with slott
# each index has three slots, one for each payment type
currentSession = []


TotalSession = 0
actualItems = 0



def LoadItemsFromData():
    file = open(ItemsPath, 'r')
    items = file.readlines() # reads all the lines and passes them to an array
    items = [item.replace('\n', '') for item in items]

    for x in range(0, len(items)):
        app = items[x] # gets the element from the item list
        app = app.split(',') # spilts it into an array with     ['name', 'price']
        app[1] = int(app[1]) # converts price to int            ['name', price]
        items[x] = app

    return items

def InitCurrentSession():
    global currentSession
    currentCart.clear()
    for i in range(0, len(LoadItemsFromData())):
        currentCart.append([0,0,0])
    print(currentCart)
InitCurrentSession()

def AddToSession():
    cart = GetCurrentCart()
    items = LoadItemsFromData()

    for item in range(0, len(items)):


def InitAndResetCart():
    global currentCart
    currentCart.clear()
    for i in range(0, len(LoadItemsFromData())):
        currentCart.append(0)
    # print(currentCart)

InitAndResetCart()


def AddToCart(num):
    global currentCart
    global currentPaymentMethod
    currentCart[num] += 1
    print(currentCart)

def ClearCart():
    c = 1

def GetCurrentCart():
    global currentCart
    return currentCart


def GetConfig(index = 0):
    file = open("config.txt", "r")
    file = file.readlines()
    file = file[index]
    file = file.replace(" ", "")  # removes spaces
    file = file.replace("\n", "")  # removes enter/\n
    file = file.split("=") # splits
    file = file[1] # gets the value/the second element
    return file

def NextCustomer():
    nextc = 1
    #goes to next customer



# external data/serializing
def SerializeItems():
    s = 1



def AddNewItemToItemsFile(name = "", price = 10):
    file = open(ItemsPath, 'a')
    file.write('\n' + name + ',' + price)

def CheckIfFileExits(string = ""):
    try:
        open(string, "x")
        return False
    except Exception:
        return True



class PaymentMethod(Enum):
    Vipps = 0
    Kontant = 1
    Kort = 2

#defualt value is Vipps
currentPaymentMethod = PaymentMethod.Vipps

def GetCurrentPaymentMethod():
    global currentPaymentMethod
    return currentPaymentMethod

def SetCurrentPaymentMethod(method = PaymentMethod):
    global currentPaymentMethod
    currentPaymentMethod = method


#print(GetCurrentPaymentMethod().value)
#SetCurrentPaymentMethod(PaymentMethod.Kontant)
#print(GetCurrentPaymentMethod().value)


