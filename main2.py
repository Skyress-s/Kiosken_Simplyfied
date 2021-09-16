from datetime import datetime
import os
from enum import Enum

ItemsPath = 'Items.txt'

currentCart = 0
TotalSession = 0
actualItems = 0


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

def AddToCart():
    addt = 1

def ClearCart():
    c = 1

# external data/serializing
def SerializeItems():
    s = 1

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

def AddNewItemToItemsFile(name = "", price = 10):
    file = open(ItemsPath, 'a')
    file.write('\n' + name + ',' + price)

def CheckIfFileExits(string = ""):
    try:
        open(string, "x")
        return False
    except Exception:
        return True



class CurrentPaymentMethod(Enum):
    Vipps = 1
    Kontant = 2
    Kort = 3

print(CurrentPaymentMethod.Kort.value)
