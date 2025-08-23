from tkinter import *
from tkinter import ttk
import json
import random
from characters import ASCII, UTF8

def printStr(length, charSet):
    for i in range(length):
        char = random.choice(charSet)
        print(char)

print(printStr(10, UTF8))

'''
root = Tk()
root.title("Random String Generator")

mainframe =  ttk.Frame(root, )
'''