import tkinter as tk
import win32gui
import win32con

def create_online_overlay(parent):
    # Ana root'a bağlı her zaman üstte duracak yeni bir pencere
    overlay = tk.Toplevel(parent)
    overlay.overrideredirect(True)
    overlay.attributes("-topmost", True)

    # Arkaplanı siyah yap ve siyahı Windows şeffaflık rengi olarak belirle
    overlay.config(bg="black")
    overlay.attributes("-transparentcolor", "black")

    # Ekranın sağ üst köşesine sabitleme
    ekran_genisligi = overlay.winfo_screenwidth()
    overlay.geometry(f"200x50+{ekran_genisligi - 150}+20")

    # Yazı tasarımı
    label = tk.Label(overlay, text="ONLINE", font=("Arial", 16, "bold"), fg="#00FF00", bg="black")
    label.pack()

    # Ekran güncellenmeden win32gui pencereyi bulamaz
    overlay.update()

    # Tıklamaların yazının içinden oyuna geçmesini sağlayan pywin32 müdahalesi
    hwnd = win32gui.GetParent(overlay.winfo_id())
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED)

    return overlay