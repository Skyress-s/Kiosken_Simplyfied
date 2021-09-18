from datetime import datetime
import os
from enum import Enum
# all global items are defined here
ItemsPath = 'Items.txt'
b_createdNewLogFile = False
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
        currentSession[i][GetCurrentPaymentMethod().value] += cart[i]
    #print(currentSession)


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


    #creates nearly full / base for file name
    logFileName = "log_" + str(datetime.today().strftime("%d_%m_%Y"))
    #checks if the file alleready exsits

    logs = []
    for file in os.listdir(path):
        if file.startswith(logFileName):
            file = file[:-4]

            file = file.split("#")
            file = int(file[1])

            logs.append(file)
    # sorts out the highest num in the files with the same name as this one
    highestnum = 0
    for num in logs:
        if num > highestnum:
            highestnum = num

    # creates a new file name based on if it alleready have done it this session
    global b_createdNewLogFile
    if b_createdNewLogFile == False:
        logFileName += "#" + str(highestnum + 1) + ".txt"
        b_createdNewLogFile = True
    else:
        logFileName += "#" + str(highestnum) + ".txt"

    path = (os.path.join(path, logFileName))

   # defining func to add number of spaces

    def addNumOfSpaces(num=0):

        spaces = ""
        for i in range(0, num):
            spaces += " "

        return spaces

    # -------------------- writes the string to write to the file

    file = open(path, 'w')

    spacing = 25
    s = ""
    s += "Amount                             Vipps,Kontant,Kort"
    s += "\n\n\n"

    for j in range(0, len(currentSession)):
        add = ""
        add += items[j][0]
        add += addNumOfSpaces(spacing - len(add))
        add += str(items[j][1])
        add += addNumOfSpaces((spacing*2) - len(add))

        for i in range(0, len(currentSession[j])):

            add += str(currentSession[j][i]) + ','

        # add the sum of the total amount for all items
        add += "        total: " + str(currentSession[j][0] + currentSession[j][1] + currentSession[j][2])

        add += '\n' # new line
        s += add # add it to the string file

        # add the sum of total amount of that item



    s += "\n\n\n"

    def SumOfOnePaymentMethod(num = 0):
        result = 0
        for i in range(0, len(items)):
            result += currentSession[i][num] * items[i][1]
        return result

    s += "Total for Vipps           : " + str(SumOfOnePaymentMethod(0)) + '\n'
    s += "Total for Kontant         : " + str(SumOfOnePaymentMethod(1)) + '\n'
    s += "Total for Kort            : " + str(SumOfOnePaymentMethod(2)) + '\n' + '\n'
    s += "Total for entire session      : " + str(SumOfOnePaymentMethod(0) + SumOfOnePaymentMethod(1) + SumOfOnePaymentMethod(2))


    file.write(s)
    file.close()



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


