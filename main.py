from datetime import datetime
import os
filepath = 'Items.txt'

b_createdNewLogFile = False


def appendItems(newItem, price):
    file = open(filepath, "a")
    enter = "\n"
    try:
        if open(filepath, "r").read() == "":
            print("file i empty")
            enter = ""

        file.write(enter + str(newItem) + "," + str(price))
    finally:
        file.close()

def aquireItems():
    file = open(filepath, 'r') # finds the items
    items = file.readlines()  #seperates each line into a list

    # but the \n is removed in the for loop? what?

    items = [item.replace('\n', '') for item in items]

    x = 0
    for item in items:
        new = items[x].split(',')  # splits the lists into lists with name and price
        new.append(0)  # adds a thrid element to the minor lists for the future amount

        items[x] = new
        x = x + 1

    return items


MinusToggle = True

def GetMinusToggle():
    global MinusToggle
    return MinusToggle

def ToggleMinusToggle():
    global MinusToggle
    if MinusToggle == True:
        MinusToggle = False
    else:
        MinusToggle = True

def purchase(index):
    global items
    global MinusToggle
    items[index][2] += (MinusToggle*2-1)
    # print(items)

def clearCart():
    global items
    for item in items:
        item[2] = 0

b_Vipps = True
def GetVippsBool():
    global b_Vipps
    return b_Vipps

def ToggleVippsBool():
    global b_Vipps
    if  b_Vipps == True:
        b_Vipps = False
    else:
        b_Vipps = True

def SetToggleVippsBool(b = True):
    global b_Vipps
    b_Vipps = b

def NextCostumer():
    addToSessionList()
    global items
    items = aquireItems()
    #print("items: " + str(items))
    #print("globalItems: " + str(globalSessionItems))
    SerilizeCurrentSession()

# this creates the item list to use further on and in the GUI
items = aquireItems()


# this creates a list for the entire session, this is what we serilize to at the end
globalSessionItems = aquireItems()

globalSessionItemsKontant = aquireItems()

# it also has a number of items sold via cash
for i in range(0, len(globalSessionItems)):
    l = globalSessionItems[i]
    l = list(l)
    l.append(0)
    globalSessionItems[i] = l
print(globalSessionItems)






def SerilizeCurrentSession():
    logFileName = "log_" + str(datetime.today().strftime("%d_%m_%Y"))

    # gets all the strings of the directory and finds the lastest log file

    directory = os.getcwd()  # current working directory
    # creates the subfolder
    path = os.path.join(directory, "logs")
    try:
        os.mkdir(path)
    except:
        print("folder alleready exists")

    # finds the numbers
    logs = []
    for file in os.listdir(path):
        if file.startswith(logFileName):
            file = file[:-4]
            file = file.split("#")
            file = int(file[1])
            logs.append(file)

    # sorts out the highest number
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

    # writes the log
    global globalSessionItems
    file = open(path, "w")
    s = ""
    # adds a description of what the placments means
    s += "itemname,price,kontant,Vipps\n\n"

    for x in range(0, len(items)):
        new = str(globalSessionItems[x][0]) + ',' + str(globalSessionItems[x][1]) + ',' + \
              str(globalSessionItems[x][2]) + ',' + str(globalSessionItems[x][3]) + "\n"
        s += new


    # adds a nice cleas sum at the bottom
    def SUM(i = 1):
        total = 0
        for x in globalSessionItems:
            num = int(x[1]) * int(x[i])
            total += num
        return total

    # adds the total of kontant and vipps

    s += "\nTotal Vipps of session is:\n" + str(SUM(3))

    s += "\nTotal kontant of session is:\n" + str(SUM(2))

    # adds the total of both
    s += "\nTotal of kontant and Vipps is:\n" + str(SUM(2) + SUM(3))

    file.write(s)
    file.close()


def addToSessionList():
    # finds out if cart is in vipps or kontant mode
    b = GetVippsBool()
    vippsKontant = 2
    if b == True:
        vippsKontant = 3
    else:
        vippsKontant = 2

    for i in range(0, len(items)):

        globalSessionItems[i][vippsKontant] += items[i][2]
    print(globalSessionItems)
    # experimental with vipps and kontant


def CheckIfFileExits(string = ""):
    try:
        open(string, "x")
        return False
    except Exception:
        return True


def GetConfig(index = 0):
    file = open("config.txt", "r")
    file = file.readlines()
    file = file[index]
    file = file.replace(" ", "")  # removes spaces
    file = file.replace("\n", "")  # removes enter/\n
    file = file.split("=") # splits
    file = file[1] # gets the value
    return file
