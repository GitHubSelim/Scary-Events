import tkinter as tk
import os
from PIL import Image, ImageTk

def setup_image_ui(image_dir, image_list):
    root = tk.Tk()
    root.withdraw() 
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg='black')

    ekran_genisligi = root.winfo_screenwidth()
    ekran_yuksekligi = root.winfo_screenheight()

    # Tüm resimlerin RAM'de tutulacağı sözlük
    preloaded_images = {}

    for img_name in image_list:
        img_path = os.path.join(image_dir, img_name)
        try:
            orijinal_resim = Image.open(img_path) 
            boyutlandirilmis = orijinal_resim.resize((ekran_genisligi, ekran_yuksekligi))
            foto = ImageTk.PhotoImage(boyutlandirilmis)
            preloaded_images[img_name] = foto
        except Exception as e:
            print(f"[HATA] {img_name} yüklenemedi: {e}")


    label = tk.Label(root, bg='black')
    label.pack(expand=True, fill="both")


    return root, label, preloaded_images