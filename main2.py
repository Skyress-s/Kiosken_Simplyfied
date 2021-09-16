from datetime import datetime
import os

currentCart = 0
TotalSession = 0
actualItems = 0


items = {1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17}

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

def LoadFromData():
    l = 1
