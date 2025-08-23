from tkinter import *
from tkinter import filedialog
import random
from characters import ASCII, UTF8

def genStr(length, charSet):
    result = ""
    for i in range(length):
        char = random.choice(charSet)
        result += char
    return result

def printStr(length, charSet):
    global generatedString
    generatedString = genStr(length, charSet)
    stringOutput = Label(root, bg="white", fg="black", text=generatedString)
    stringOutput.pack()

def sel():
    global charSet
    if selected_option.get() == "utf8":
        charSet = UTF8
    elif selected_option.get() == "ascii":
        charSet = ASCII

def save():
    if generatedString:
        fileDialog = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )

        if fileDialog:
            with open(fileDialog, 'w') as f:
                f.write(generatedString)

root = Tk()
root.title("Random String Generator")
root.geometry("300x275")

selected_option = StringVar(value="utf8")
charSet = UTF8

lengthLabel = Label(root, text="Enter a number:")
lengthLabel.pack(padx=5, pady=5)

lengthInput = Entry(root, width=3)
lengthInput.insert(0, "10")
lengthInput.pack(padx=5, pady=5)

charLabel = Label(root, text="Choose a character set:")
charLabel.pack(pady=(20, 5))

rbtnUTF8 = Radiobutton(root, text="UTF-8", variable=selected_option, value="utf8", command=sel)
rbtnUTF8.pack(pady=2)
rbtnASCII = Radiobutton(root, text="ASCII", variable=selected_option, value="ascii", command=sel)
rbtnASCII.pack(pady=2)

frameBtn = Frame(root)
frameBtn.pack(pady=20)

btnGenerate = Button(frameBtn, text="Generate string", command= lambda: printStr(int(lengthInput.get()), charSet))
btnGenerate.pack(side="left", padx=5)
btnSave = Button(frameBtn, text="Save to file", command=save)
btnSave.pack(side="left", padx=5)

root.mainloop()