from datetime import datetime
import os
from enum import Enum
# all global items are defined here
ItemsPath = 'Items.txt'

currentCart = [] # has this form currentcart[index][currentPaymentMethod] ie. index 0 = solo 1 = pepsi, cPM it with slott
# each index has three slots, one for each payment type
currentSession = []




def LoadItemsFromData():
    file = open(ItemsPath, 'r')
    items = file.readlines() # reads all the lines and passes them to an array
    items = [item.replace('\n', '') for item in items]

    for x in range(0, len(items)):
        app = items[x] # gets the element from the item list
        app = app.split(',') # spilts it into an array with     ['name', 'price']
        app[1] = int(app[1]) # converts price to int            ['name', price]
        items[x] = app

    file.close()
    return items

def InitCurrentSession():
    global currentSession
    currentCart.clear()
    for i in range(0, len(LoadItemsFromData())):
        currentSession.append([0,0,0])
    #print(currentSession)
InitCurrentSession()


def AddToSession():
    global currentSession
    cart = GetCurrentCart()
    items = LoadItemsFromData()

    for i in range(0, len(items)):
        currentSession[i][GetCurrentPaymentMethod().value] = cart[i]
    print(currentSession)


def SerializeSession():
    #get the relevant items
    items = LoadItemsFromData()
    global currentSession

    # creates the subfolder
    directory = os.getcwd()
    path = os.path.join(directory, "logs")
    try:
        os.mkdir(path)
    except:
        print("folder alleready exists")

    logFileName = "log_" + str(datetime.today().strftime("%d_%m_%Y"))
    logs = []
    for file in os.listdir(path):
        if file.startswith(logFileName):
            file = file[:-4]
            file = file.split("#")
            file = int(file[1])
            logs.append(file)


    # writes the string to write to the file
    s = ""
    for j in range(0, len(currentSession)):
        s += items[j][0] + ','
        for i in range(0, len(currentSession[j])):
            print(currentSession[j][i])
            s += str(currentSession[j][i]) + ','
        s += '\n'







SerializeSession()


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
    #print(currentCart)

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


