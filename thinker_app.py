# Der Benutzer muss ein Bild/ PDF hochladen koennen.
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Step 1
#eine User Interface erstellen mit Tkinter, mit ein knopf "Datei hochladen".
# da koennen wir zum Beispiel eine Variabel definieren.


def open_Image():
    #Oeffnung des Fensters mit Bildauswahl
    filepath= filedialog.LoadFileDialog(filetypes=[('Image files', '*.jpg; *.png;*jpeg')])
    if filepath :
        image= Image.open(filepath)
