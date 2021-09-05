import tkinter as tk
from tkinter import filedialog

from cipher.vigenere import vigenere_encrypt, vigenere_decrypt
from cipher.vigenere_full import generate_full_vigenere_matrix, vigenere_full_encrypt, vigenere_full_decrypt
from cipher.vigenere_autokey import vigenere_autokey_encrypt, vigenere_autokey_decrypt
from cipher.vigenere_extended import vigenere_extended_encrypt, vigenere_extended_decrypt
from cipher.playfair import playfair_encrypt, playfair_decrypt
from cipher.affine import affine_encrypt, affine_decrypt
from cipher.hill import hill_decrypt, hill_decrypt, hill_encrypt

# util
filepath = ""

def spaceFive(text) :
    out = [text[i:i+5] for i in range(0, len(text), 5)]
    out = ' '.join(out)
    return out

def importFile():
  file = filedialog.askopenfile(mode="r")
  if file is not None:
    fileContent = file.read()

  inputText.delete("0.0", "end")
  inputText.insert("0.0", fileContent)

def exportFile():
  out = outputText.get("0.0", "end-1c")
  with open("test_file/output.txt", "w") as file:
    file.write(out)

def runProgram():
  algoChoice = algoRadVar.get()
  opChoice = opRadVar.get()
  spaceChoice = spaceCheckVar.get()
  input = inputText.get("0.0", "end-1c")
  key = keyEntry.get()

  out = ""

  if (algoChoice == 1): # vigenere standard
    if (opChoice == 1):
      out = vigenere_encrypt(input, key)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = vigenere_decrypt(input, key)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 2): # full vigenere
    encryptMatrix = generate_full_vigenere_matrix()

    if (opChoice == 1):
      out = vigenere_full_encrypt(input, key, encryptMatrix)

      if (spaceChoice == 1):
        out = spaceFive(out)

      matEncText.config(state="normal")
      matEncText.delete("0.0", "end")
      matEncText.insert("0.0", encryptMatrix)
      matEncText.config(state="disabled")
    elif (opChoice == 2):
      decryptMatrix = matDecText.get("0.0", "end-1c")
      decryptMatrix = list(decryptMatrix.split(" "))

      out = vigenere_full_decrypt(input, key, decryptMatrix)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 3): # auto-key vigenere
    if (opChoice == 1):
      out = vigenere_autokey_encrypt(input, key)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = vigenere_autokey_decrypt(input, key)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 4): # extended vigenere
    if (opChoice == 1):
      out = vigenere_extended_encrypt(input, key)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = vigenere_extended_decrypt(input, key)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 5): # extended vigenere file
    filepath = filedialog.askopenfilename()
    inputFile = open(filepath, "rb")
    data = inputFile.read()
    data = data.decode("latin-1")
    inputFile.close()

    if (opChoice == 1):
      out = vigenere_extended_encrypt(data, key)
    elif (opChoice == 2):
      out = vigenere_extended_decrypt(data, key)
    
    out = out.encode("latin-1")
    outputFile = open(filepath, "wb")
    outputFile.write(out)
    outputFile.close()
  elif (algoChoice == 6): # playfair
    if (opChoice == 1):
      out = playfair_encrypt(input, key)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = playfair_decrypt(input, key)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 7): # affine
    key = int(key)
    key_b = int(keyBEntry.get())

    if (opChoice == 1):
      out = affine_encrypt(input, key, key_b)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = affine_decrypt(input, key, key_b)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")
  elif (algoChoice == 8): # hill
    if (opChoice == 1):
      out = hill_encrypt(input, key)
      
      if (spaceChoice == 1):
        out = spaceFive(out)
    elif (opChoice == 2):
      out = hill_decrypt(input, key)
    
    outputText.config(state="normal")
    outputText.delete("0.0", "end")
    outputText.insert("0.0", out)
    outputText.config(state="disabled")

# root
root = tk.Tk()
root.title("Tugas 1 Kripto")
root.resizable(False, False)

## top frame
topFrame = tk.Frame(root, padx=25, pady=15)
topFrame.grid(row=0, column=0)

# input textbox
inputLabel = tk.Label(topFrame, text="Input Text")
inputLabel.grid(row=0, column=0)
inputText = tk.Text(topFrame, height=20, width=20)
inputText.grid(row=1, column=0)

# vigenere matrix input textbox
matDecLabel = tk.Label(topFrame, text="Full Vigenere Decryption Matrix")
matDecLabel.grid(row=0, column=1)
matDecText = tk.Text(topFrame, height=20, width=20)
matDecText.grid(row=1, column=1)

# vigenere matrix output textbox
matEncLabel = tk.Label(topFrame, text="Full Vigenere Encryption Matrix")
matEncLabel.grid(row=0, column=2)
matEncText = tk.Text(topFrame, height=20, width=20, state="disabled")
matEncText.grid(row=1, column=2)

# output textbox
outputLabel = tk.Label(topFrame, text="Output Text")
outputLabel.grid(row=0, column=3)
outputText = tk.Text(topFrame, height=20, width=20, state="disabled")
outputText.grid(row=1, column=3)

## bot frame
botFrame = tk.Frame(root, padx=25, pady=15)
botFrame.grid(row=1, column=0)

# key choice
keyLabel = tk.Label(botFrame, text="Key")
keyLabel.grid(row=0, column=0, sticky="w")
keyEntry = tk.Entry(botFrame)
keyEntry.grid(row=0, column=1, sticky="w")
keyBLabel = tk.Label(botFrame, text="Key B")
keyBLabel.grid(row=1, column=0, sticky="W")
keyBEntry = tk.Entry(botFrame)
keyBEntry.grid(row=1, column=1, sticky="w")

# io button
importBtn = tk.Button(botFrame, text="Import File", command=lambda:importFile())
importBtn.grid(row=2, column=0, sticky="w")
exportBtn = tk.Button(botFrame, text="Export File", command=lambda:exportFile())
exportBtn.grid(row=3, column=0, sticky="w")

# cipher choice
algoRadVar = tk.IntVar()
vigeStdRadBtn = tk.Radiobutton(botFrame, text="Standar Vigenere Cipher", variable=algoRadVar, value=1)
vigeStdRadBtn.grid(row=0, column=2, sticky="w")
vigeFullRadBtn = tk.Radiobutton(botFrame, text="Full Vigenere Cipher", variable=algoRadVar, value=2)
vigeFullRadBtn.grid(row=1, column=2, sticky="w")
vigeAutoRadBtn = tk.Radiobutton(botFrame, text="Auto-key Vigenere Cipher", variable=algoRadVar, value=3)
vigeAutoRadBtn.grid(row=2, column=2, sticky="w")
vigeExtRadBtn = tk.Radiobutton(botFrame, text="Extended Vigenere Cipher", variable=algoRadVar, value=4)
vigeExtRadBtn.grid(row=3, column=2, sticky="w")
vigeExtFileRadBtn = tk.Radiobutton(botFrame, text="Extended Vigenere Cipher (File)", variable=algoRadVar, value=5)
vigeExtFileRadBtn.grid(row=0, column=3, sticky="w")
playfairRadBtn = tk.Radiobutton(botFrame, text="Playfair Cipher", variable=algoRadVar, value=6)
playfairRadBtn.grid(row=1, column=3, sticky="w")
affineRadBtn = tk.Radiobutton(botFrame, text="Affine Cipher", variable=algoRadVar, value=7)
affineRadBtn.grid(row=2, column=3, sticky="w")
hillRadBtn = tk.Radiobutton(botFrame, text="Hill Cipher", variable=algoRadVar, value=8)
hillRadBtn.grid(row=3, column=3, sticky="w")

# operation
opRadVar = tk.IntVar()
encryptRadBtn = tk.Radiobutton(botFrame, text="Encrypt", variable=opRadVar, value=1)
encryptRadBtn.grid(row=0, column=5, sticky="w")
decryptRadBtn = tk.Radiobutton(botFrame, text="Decrypt", variable=opRadVar, value=2)
decryptRadBtn.grid(row=1, column=5, sticky="w")

spaceCheckVar = tk.IntVar()
spaceCheckBtn = tk.Checkbutton(botFrame, text="Spaced?", variable=spaceCheckVar, onvalue=1, offvalue=0)
spaceCheckBtn.grid(row=2, column=5, sticky="w")

# run
runBtn = tk.Button(botFrame, text="Run Program", command=lambda:runProgram())
runBtn.grid(row=0, column=6, sticky="w")

root.mainloop()