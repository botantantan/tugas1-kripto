# IF4020 Kriptografi
## Tugas 1

Tugas berikut merupakan implementasi dari beberapa algoritma untuk melakukan enkripsi dan dekripsi dari sebuah teks atau file

Algoritma yang diujikan berupa:
- Vigenere Cipher Standard (26 huruf alfabet)
- Full Vigenere Cipher (26 huruf alfabet)
- Auto-Key Vigenere Cipher (26 huruf alfabet)
- Extended Vigenere Cipher (256 karakter ASCII)
- Playfair Cipher (26 huruf alfabet)
- Affine Cipher (26 huruf alfabet)
- Hill Cipher

## Prerequisite
Module yang dibutuhkan dalam program ini:
- tkinter
  ```
  pip install tk
  ```

## Cara Menjalankan Program
```
python main.py
```

## Catatan
Untuk fitur Extended Vigenere Cipher (File) dapat menyebabkan crash jika dijalankan melalui GUI, untuk menjalankan fitur harus melalui terminal dengan cara:
```
python vigenere_extended.py
```
Sebelum menjalankan command tersebut: 
- Unblock terlebih dahulu `line 46-61`
- Mengganti value dari `flag` dengan `True` untuk enkripsi dan `False` untuk dekripsi
- Mengganti file yang diingin dienkripsi atau dekripsi di `line 46` dengan absolute atau relatif path dari file tersebut

## Tugas ini dikerjakan oleh
- Fritz Gerald Tjie - 13518065
- Byan Sakura Kireyna Aji - 13518066