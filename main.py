from tkinter import *
from tkinter import filedialog
import random
import string

def genStr(length, charset_type):
    if charset_type == "ascii":
        chars = string.printable.rstrip('\t\n\r\x0b\x0c')
        return ''.join(random.choices(chars, k=length))
    else:
        utf8_ranges = [
            (0x0020, 0x007E),   # Basic Latin
            (0x00A0, 0x00FF),   # Latin-1 Supplement
            (0x0100, 0x017F),   # Latin Extended-A
            (0x2000, 0x206F),   # General Punctuation
            (0x20A0, 0x20CF),   # Currency Symbols
        ]
        
        result = []
        for _ in range(length):
            start, end = random.choice(utf8_ranges)
            while True:
                code_point = random.randint(start, end)
                if not (0xD800 <= code_point <= 0xDFFF):
                    try:
                        char = chr(code_point)
                        result.append(char)
                        break
                    except ValueError:
                        continue
        return ''.join(result)

def printStr(length, charset_type):
    global generatedString
    generatedString = genStr(length, charset_type)
    stringOutput = Label(root, bg="white", fg="black", text=generatedString)
    stringOutput.pack()

def save():
    if generatedString:
        fileDialog = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )
        if fileDialog:
            with open(fileDialog, 'w', encoding='utf-8') as f:
                f.write(generatedString)

root = Tk()
root.title("Random String Generator")
root.geometry("300x275")

selected_option = StringVar(value="utf8")

lengthLabel = Label(root, text="Enter a number:")
lengthLabel.pack(padx=5, pady=5)

lengthInput = Entry(root, width=3)
lengthInput.insert(0, "10")
lengthInput.pack(padx=5, pady=5)

charLabel = Label(root, text="Choose a character set:")
charLabel.pack(pady=(20, 5))

rbtnUTF8 = Radiobutton(root, text="UTF-8", variable=selected_option, value="utf8")
rbtnUTF8.pack(pady=2)
rbtnASCII = Radiobutton(root, text="ASCII", variable=selected_option, value="ascii")
rbtnASCII.pack(pady=2)

frameBtn = Frame(root)
frameBtn.pack(pady=20)

btnGenerate = Button(frameBtn, text="Generate string", command=lambda: printStr(int(lengthInput.get()), selected_option.get()))
btnGenerate.pack(side="left", padx=5)
btnSave = Button(frameBtn, text="Save to file", command=save)
btnSave.pack(side="left", padx=5)

root.mainloop()