from datetime import datetime
import os


items = {1,2,3,4,5,6}

def GetConfig(index = 0):
    file = open("config.txt", "r")
    file = file.readlines()
    file = file[index]
    file = file.replace(" ", "")  # removes spaces
    file = file.replace("\n", "")  # removes enter/\n
    file = file.split("=") # splits
    file = file[1] # gets the value
    return file