from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract



# Configuration de Tesseract (assurez-vous que le chemin est correct pour votre système)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Pour Windows

# Fonction pour ouvrir un fichier image et extraire le texte
def ouvrir_image():
    # Ouvre la boîte de dialogue pour sélectionner une image
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if filepath:
        # Charger l'image et utiliser Tesseract pour extraire le texte
        image = Image.open(filepath)
        texte = pytesseract.image_to_string(image)
        # Afficher le texte extrait dans le label
        label_resultat.config(text=texte)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("OCR - Extraction de Texte d'une Image")

# Bouton pour ouvrir une image
button_ouvrir = tk.Button(fenetre, text="Ouvrir une image", command=ouvrir_image)
button_ouvrir.pack(pady=10)

# Label pour afficher le texte extrait
label_resultat = tk.Label(fenetre, text="Le texte extrait apparaîtra ici.", font=('Arial', 12), justify="left")
label_resultat.pack(pady=10, padx=20)

# Lancer l'application
fenetre.mainloop()
