import tkinter as tk
from tkinter import Text, filedialog

# util
def importFile():
  file = filedialog.askopenfile(mode="r")
  if file is not None:
    fileContent = file.read()

  inputText.delete("0.0", "end")
  inputText.insert("0.0", fileContent)

  encryptText.config(state="normal")
  encryptText.delete("0.0", "end")
  encryptText.insert("0.0", fileContent)
  encryptText.config(state="normal")

def exportFile():
  outE = encryptText.get("0.0", "end-1c")
  with open("encryptText.txt", "w") as file:
    file.write(outE)
  
  outD = decryptText.get("0.0", "end-1c")
  with open("decryptText.txt", "w") as file:
    file.write(outD)

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

encryptLabel = tk.Label(topFrame, text="Encrypted Text")
encryptLabel.grid(row=0, column=1)
encryptText = tk.Text(topFrame, height=25, width=30, state="disabled")
encryptText.grid(row=1, column=1)

decryptLabel = tk.Label(topFrame, text="Decrypted Text")
decryptLabel.grid(row=0, column=2)
decryptText = tk.Text(topFrame, height=25, width=30, state="disabled")
decryptText.grid(row=1, column=2)

## bot frame
botFrame = tk.Frame(root, padx=25, pady=15)
botFrame.grid(row=1, column=0)

key1Label = tk.Label(botFrame, text="Key 1")
key1Label.grid(row=0, column=0)
key1Text = tk.Entry(botFrame)
key1Text.grid(row=0, column=1, sticky="w")
key2Label = tk.Label(botFrame, text="Key 2")
key2Label.grid(row=1, column=0)
key2Text = tk.Entry(botFrame)
key2Text.grid(row=1, column=1, sticky="w")

importBtn = tk.Button(botFrame, text="Import File", command=lambda:importFile())
importBtn.grid(row=2, column=0)
exportBtn = tk.Button(botFrame, text="Export File", command=lambda:exportFile())
exportBtn.grid(row=2, column=1)

algoChoice = tk.IntVar()
vigeStdRadBtn = tk.Radiobutton(botFrame, text="Standar Vigenere Cipher", variable=algoChoice, value=1)
vigeStdRadBtn.grid(row=0, column=2, sticky="w")
vigeFullRadBtn = tk.Radiobutton(botFrame, text="Full Vigenere Cipher", variable=algoChoice, value=2)
vigeFullRadBtn.grid(row=1, column=2, sticky="w")
vigeAutoRadBtn = tk.Radiobutton(botFrame, text="Auto-key Vigenere Cipher", variable=algoChoice, value=3)
vigeAutoRadBtn.grid(row=2, column=2, sticky="w")
vigeExtRadBtn = tk.Radiobutton(botFrame, text="Extended Vigenere Cipher", variable=algoChoice, value=4)
vigeExtRadBtn.grid(row=0, column=3, sticky="w")
playfairRadBtn = tk.Radiobutton(botFrame, text="Playfair Cipher", variable=algoChoice, value=5)
playfairRadBtn.grid(row=1, column=3, sticky="w")
affineRadBtn = tk.Radiobutton(botFrame, text="Affine Cipher", variable=algoChoice, value=6)
affineRadBtn.grid(row=2, column=3, sticky="w")

runBtn = tk.Button(botFrame, text="Run Program")
runBtn.grid(row=1, column=4)

root.mainloop()

