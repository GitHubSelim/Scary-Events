import tkinter as tk

def create_online_overlay(parent):
    # Ana root'a bağlı her zaman üstte duracak yeni bir pencere
    overlay = tk.Toplevel(parent)
    overlay.overrideredirect(True)
    overlay.attributes("-topmost", True)

    # Arkaplanı siyah yap ve siyahı Windows şeffaflık rengi olarak belirle
    overlay.config(bg="black")
    # overlay.attributes("-transparentcolor", "black")

    # Ekranın sağ üst köşesine sabitleme
    ekran_genisligi = overlay.winfo_screenwidth()
    overlay.geometry(f"200x50+{ekran_genisligi - 150}+20")

    # Yazı tasarımı
    label = tk.Label(overlay, text="ONLINE", font=("Arial", 16, "bold"), fg="#00FF00", bg="black")
    label.pack()

    # Ekran güncellenmeden win32gui pencereyi bulamaz
    overlay.update()

    return overlay
