import tkinter as tk
from tkinter import filedialog

from vigenere import vigenere_encrypt, vigenere_decrypt
from vigenere_full import generate_full_vigenere_matrix, vigenere_full_encrypt, vigenere_full_decrypt
from vigenere_autokey import vigenere_autokey_encrypt, vigenere_autokey_decrypt
from vigenere_extended import vigenere_extended_encrypt, vigenere_extended_decrypt
from playfair import playfair_encrypt, playfair_decrypt
from affine import affine_encrypt, affine_decrypt
from hill import hill_decrypt, hill_decrypt, hill_encrypt

# util
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
  outVI = vigeMatrixInputText.get("0.0", "end-1c")
  with open("test_file/fullVigeMatrixInput.txt", "w") as file:
    file.write(outVI)

  outVO = vigeMatrixOutputText.get("0.0", "end-1c")
  with open("test_file/fullVigeMatrixOutput.txt", "w") as file:
    file.write(outVO)

  outE = encryptText.get("0.0", "end-1c")
  with open("test_file/encryptText.txt", "w") as file:
    file.write(outE)
  
  outD = decryptText.get("0.0", "end-1c")
  with open("test_file/decryptText.txt", "w") as file:
    file.write(outD)

  outDSpace = decryptSpaceText.get("0.0", "end-1c")
  with open("test_file/decryptSpaceText.txt", "w") as file:
    file.write(outDSpace)

def runProgram():
  algoChoice = radioVar.get()
  input = inputText.get("0.0", "end-1c")
  key = key1Text.get()

  if (algoChoice == 1): # vigenere standard
    encryptedText = vigenere_encrypt(input, key)
    decryptedText = vigenere_decrypt(input, key)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 2): # full vigenere
    fullVigeMatrix = generate_full_vigenere_matrix()

    vigeMatrixOutputText.config(state="normal")
    vigeMatrixOutputText.delete("0.0", "end")
    vigeMatrixOutputText.insert("0.0", fullVigeMatrix)
    vigeMatrixOutputText.config(state="disabled")

    inputMatrix = vigeMatrixInputText.get("0.0", "end-1c")
    decryptMatrix = list(inputMatrix.split(" "))

    encryptedText = vigenere_full_encrypt(input, key, fullVigeMatrix)
    decryptedText = vigenere_full_decrypt(input, key, decryptMatrix)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 3): # auto-key vigenere
    encryptedText = vigenere_autokey_encrypt(input, key)
    decryptedText = vigenere_autokey_decrypt(input, key)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 4): # extended vigenere
    encryptedText = vigenere_extended_encrypt(input, key)
    decryptedText = vigenere_extended_decrypt(input, key)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 5): # playfair
    encryptedText = playfair_encrypt(input, key)
    decryptedText = playfair_decrypt(input, key)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 6): # affine
    key = int(key)
    key_b = int(key2Text.get())

    print(type(key))
    print(key)
    print(type(key_b))
    print(key_b)
    
    encryptedText = affine_encrypt(input, key, key_b)
    decryptedText = affine_decrypt(input, key, key_b)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")
  elif (algoChoice == 7): # hill
    encryptedText = hill_encrypt(input, key)
    decryptedText = hill_decrypt(input, key)
    decryptedSpaceText = spaceFive(decryptedText)

    encryptText.config(state="normal")
    encryptText.delete("0.0", "end")
    encryptText.insert("0.0", encryptedText)
    encryptText.config(state="disabled")

    decryptText.config(state="normal")
    decryptText.delete("0.0", "end")
    decryptText.insert("0.0", decryptedText)
    decryptText.config(state="disabled")

    decryptSpaceText.config(state="normal")
    decryptSpaceText.delete("0.0", "end")
    decryptSpaceText.insert("0.0", decryptedSpaceText)
    decryptSpaceText.config(state="disabled")

# root
root = tk.Tk()
root.title("Tugas 1 Kripto")
root.resizable(False, False)

## top frame
topFrame = tk.Frame(root, padx=25, pady=15)
topFrame.grid(row=0, column=0)

inputLabel = tk.Label(topFrame, text="Input Text")
inputLabel.grid(row=0, column=0)
inputText = tk.Text(topFrame, height=25, width=30)
inputText.grid(row=1, column=0)

vigeMatrixInputLabel = tk.Label(topFrame, text="Full Vigenere Matrix Input")
vigeMatrixInputLabel.grid(row=0, column=1)
vigeMatrixInputText = tk.Text(topFrame, height=25, width=30)
vigeMatrixInputText.grid(row=1, column=1)

vigeMatrixOutputLabel = tk.Label(topFrame, text="Full Vigenere Matrix Output")
vigeMatrixOutputLabel.grid(row=0, column=2)
vigeMatrixOutputText = tk.Text(topFrame, height=25, width=30, state="disabled")
vigeMatrixOutputText.grid(row=1, column=2)

encryptLabel = tk.Label(topFrame, text="Encrypted Text")
encryptLabel.grid(row=0, column=3)
encryptText = tk.Text(topFrame, height=25, width=30, state="disabled")
encryptText.grid(row=1, column=3)

decryptLabel = tk.Label(topFrame, text="Decrypted Text")
decryptLabel.grid(row=0, column=4)
decryptText = tk.Text(topFrame, height=25, width=30, state="disabled")
decryptText.grid(row=1, column=4)

decryptSpaceLabel = tk.Label(topFrame, text="Decrypted Spaced Text")
decryptSpaceLabel.grid(row=0, column=5)
decryptSpaceText = tk.Text(topFrame, height=25, width=30, state="disabled")
decryptSpaceText.grid(row=1, column=5)

## bot frame
botFrame = tk.Frame(root, padx=25, pady=15)
botFrame.grid(row=1, column=0)

key1Label = tk.Label(botFrame, text="Key 1")
key1Label.grid(row=0, column=0)
key1Text = tk.Entry(botFrame)
key1Text.grid(row=0, column=1, sticky="w")
key2Label = tk.Label(botFrame, text="Key B (Affine Cipher)")
key2Label.grid(row=1, column=0)
key2Text = tk.Entry(botFrame)
key2Text.grid(row=1, column=1, sticky="w")

importBtn = tk.Button(botFrame, text="Import File", command=lambda:importFile())
importBtn.grid(row=2, column=0)
exportBtn = tk.Button(botFrame, text="Export File", command=lambda:exportFile())
exportBtn.grid(row=2, column=1)

radioVar = tk.IntVar()
vigeStdRadBtn = tk.Radiobutton(botFrame, text="Standar Vigenere Cipher", variable=radioVar, value=1)
vigeStdRadBtn.grid(row=0, column=2, sticky="w")
vigeFullRadBtn = tk.Radiobutton(botFrame, text="Full Vigenere Cipher", variable=radioVar, value=2)
vigeFullRadBtn.grid(row=1, column=2, sticky="w")
vigeAutoRadBtn = tk.Radiobutton(botFrame, text="Auto-key Vigenere Cipher", variable=radioVar, value=3)
vigeAutoRadBtn.grid(row=2, column=2, sticky="w")
vigeExtRadBtn = tk.Radiobutton(botFrame, text="Extended Vigenere Cipher", variable=radioVar, value=4)
vigeExtRadBtn.grid(row=0, column=3, sticky="w")
playfairRadBtn = tk.Radiobutton(botFrame, text="Playfair Cipher", variable=radioVar, value=5)
playfairRadBtn.grid(row=1, column=3, sticky="w")
affineRadBtn = tk.Radiobutton(botFrame, text="Affine Cipher", variable=radioVar, value=6)
affineRadBtn.grid(row=2, column=3, sticky="w")
hillRadBtn = tk.Radiobutton(botFrame, text="Hill Cipher", variable=radioVar, value=7)
hillRadBtn.grid(row=0, column=4, sticky="w")

runBtn = tk.Button(botFrame, text="Run Program", command=lambda:runProgram())
runBtn.grid(row=1, column=4, sticky="w")

root.mainloop()