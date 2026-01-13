import sys
import customtkinter as ctk
from PIL import ImageTk, Image
from withoutbg import WithoutBG
from tkinter import filedialog
from pathlib import Path


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Background Remover")
        self.geometry("900x600")
        self.OS=None

        # Crea il frame principale
        self.main_frame = ctk.CTkFrame(self)
        # Allargo il frame in modo tale che riempia tutta la pagina
        self.main_frame.pack(fill="both", expand=True)

        # su Windows
        if sys.platform.startswith("win"):
            self.OS="win"
            self.iconbitmap("logoBackgroundRemoverCD.ico")
        # su Mac o Linux
        else:
            self.OS = "other"
            icona = ImageTk.PhotoImage(file="logoBackgroundRemoverCD.png")
            self.wm_iconphoto(False, icona)

        # Title label
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            bg_color="transparent",
            text="Welcome To BackGroundRemover CD",
            font=("Arial", 60, "bold"),
            anchor="center"  # Centra il testo
        )
        self.title_label.pack(pady=20, padx=20, )

        # Frame contenitore
        self.father_frame = ctk.CTkFrame(self.main_frame, bg_color="transparent", fg_color="transparent")
        self.father_frame.pack(pady=20, padx=20, fill="x")

        # Frame Sotto
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.bottom_frame.pack(side="bottom", pady=20, padx=20, fill="x")

        # Griglia di contenimento dei frame
        self.container_grid = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.container_grid.pack(pady=10)

        # Label 'Inserisci foto'
        self.text_insert = ctk.CTkLabel(
            self.father_frame,
            text="Insert photo path: ",
            font=("Arial", 30)
        )
        self.text_insert.pack(side="left", padx=20)

        # TextBox del path della foto
        self.path_textbox = ctk.CTkTextbox(
            self.father_frame,
            width=700,
            height=10,
            corner_radius=15,
            text_color="white",
            font=("Arial", 15)
        )
        self.path_textbox.pack(side="left", padx=20)

        # Bottone di ricerca del path
        self.button_search = ctk.CTkButton(
            self.father_frame,
            width=140,
            height=50,
            corner_radius=15,
            text="Search",
            font=("Arial", 20),
            text_color="white",
            hover_color="#e9f0f6",
            command=self.find_path
        )
        self.button_search.pack(side="left", padx=20)

        # Bottone che avvia la rimozione del background
        self.button_remove = ctk.CTkButton(
            self.bottom_frame,
            200,
            50,
            15,
            bg_color="transparent",
            text="Remove",
            font=("Arial", 20),
            command=self.create_image,
            text_color="white",
            hover_color="white",
        )

        # Label per anteprima delle immagini
        self.image_label = ctk.CTkLabel(self.container_grid, text="")
        self.image_withoutBG_label = ctk.CTkLabel(self.container_grid, text="")

        # Variabile path dell'immagine
        self.image_path_var=None

        #Variabile per il display della cartella ove si trova il nuovo file
        self.final_path_text = ctk.CTkLabel(
            self.bottom_frame,
            text="",
            font=("Arial", 20)
        )

    # Azione bottone 'search'
    def find_path(self):

        self.path_textbox.delete(0.0, "end")

        # Apertura Scheda delle directory
        line = filedialog.askopenfilename()

        # Scrittura su textbox del path dell'immagine
        self.path_textbox.insert(0.0, line)

        # Rimozione di display precedenti
        # Controlla se l'attributo esiste per evitare errori se la funzione viene chiamata prima della creazione
        if hasattr(self, 'image_label'):
            self.image_label.grid_forget()
        if hasattr(self, 'image_withoutBG_label'):
            self.image_withoutBG_label.grid_forget()
        self.nascondi_messaggio()

        img_file = Image.open(line)

        # Settaggio delle dimensioni
        img_size = img_file.size
        img_size=self.set_sizes(img_size)

        # Mostra il bottone una volta selezionata l'immagine
        self.button_remove.pack(side="bottom", padx=20)

        # Anteprima immagine
        image = ctk.CTkImage(light_image=img_file, dark_image=img_file, size=img_size)
        self.image_label.configure(image=image)
        self.image_label.grid(row=0, column=0, padx=60)

        self.image_path_var=line

    # Creazione dell'immagine senza background
    def create_image(self):
        img = WithoutBG.opensource()
        photo_path = self.image_path_var

        # Settaggio del nome finale della foto senza sfondo
        file_name=self.find_file_name(self.image_path_var)
        file_name=file_name+"_WithoutBackground.png"

        # Rimozione dello sfondo della foto
        result = img.remove_background(photo_path)

        # Download e salvataggio della foto nella cartella 'Download'
        download_path= str(Path.home() / "Downloads" / file_name)
        result.save(download_path)

        # Apertura e settaggio dimensioni dell'anteprima senza sfondo
        img_file = Image.open(download_path)
        img_size = img_file.size
        img_size=self.set_sizes(img_size)
        
        # Anteprima immagine senza background
        image = ctk.CTkImage(light_image=img_file, dark_image=img_file, size=img_size)
        self.image_withoutBG_label.configure(image=image)
        self.image_withoutBG_label.grid(row=0, column=1, padx=60)

        # Mostra il percorso nel quale è stata salvata l'immagine
        self.final_path_text.configure(text="Immagine creata e salvata al percorso: " + download_path)
        self.final_path_text.pack(padx=20)

        self.button_remove.pack_forget()


    # Definizione dimensioni dell'immagine
    def set_sizes(self,img_size):
        less_percent=0
        while img_size[0]>1000 or img_size[1]>1000:
            # Diminuzione dell'immagine nel caso sia troppo grande
            if img_size[0] >= 200 and img_size[1] >= 200:
                img_width_size = int(img_size[0] - ((img_size[0] * (75-less_percent)) / 100))
                img_height_size = int(img_size[1] - ((img_size[1] * (75-less_percent)) / 100))
                img_size = (img_width_size, img_height_size)

            # Ingrandimento dell'immagine nel caso sia troppo piccola
            else:
                img_width_size = int(img_size[0] + ((img_size[0] * (75+less_percent)) / 100))
                img_height_size = int(img_size[1] + ((img_size[1] * (75+less_percent)) / 100))
                img_size = (img_width_size, img_height_size)

            less_percent=35

        return img_size

    # Funzione per estrapolare il nome del file
    def find_file_name(self,path):
        file_name=None
        if self.OS=='win':
            divided_path = path.split('\\')
        else:
            divided_path=path.split('/')
        for directory in divided_path:
            file_name=directory
        name_without_format=file_name.split('.')
        return name_without_format[0]

    # Nasconde final_path_text quando si va a modificare un altra immagine
    def nascondi_messaggio(self):
        # Controlla se l'attributo esiste per evitare errori se la funzione viene chiamata prima della creazione
        if hasattr(self, 'final_path_text'):
            self.final_path_text.pack_forget()

