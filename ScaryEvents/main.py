from pynput import keyboard
from pynput.keyboard import Key

import tkinter as tk
from PIL import Image, ImageTk

import pygame
import os

from load_image import setup_image_ui
from audio_manager import set_game_mute
from overlay_manager import create_online_overlay
from image_selector import pick_random_image

############################################################################################################################

def rescue_mission():
	print("You have been saved!")
	
	set_game_mute(TARGET_GAME, 1)
	try:
		pygame.mixer.music.load(MP3_FILE)
		pygame.mixer.music.play(-1)
		
	except Exception as e:
		print(f"Müzik dosyasi yükleme hatasi: {e}")

	picked_img = pick_random_image(IMAGE_WEIGHTS)
	print(f"Ekrana gelen resim: {picked_img}")
	
	image_label.config(image=preloaded_images[picked_img])
	image_label.image = preloaded_images[picked_img]
	root.deiconify()

##############################################################

def end_mission():
	print("Ending mission.")
	
	pygame.mixer.music.stop()
	set_game_mute(TARGET_GAME, 0)
	root.withdraw()

##############################################################

def quit_program():
	print("Program kapandi.")
	
	set_game_mute(TARGET_GAME, 0)
	pygame.mixer.music.stop()
	root.quit()
	root.destroy()

##############################################################

def on_release(key):
	if key == Key.esc:
		print("Exiting...")
		root.after(0, quit_program)
		return False

	elif hasattr(key, "char") and (key.char == "-" or key.char == "_"):
		print("Rescue mission initiated.")
		root.after(0, rescue_mission)

	elif key == Key.enter:
		print("Continueing to listen")
		root.after(0, end_mission)

############################################################################################################################

if __name__ == "__main__":

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	TARGET_GAME = "Backrooms-Win64-Shipping.exe"
	MP3_FILE = os.path.join(BASE_DIR, "assets", "Grieg - Morning Mood(flute).mp3")
	IMAGE_DIR = os.path.join(BASE_DIR, "assets", "ImagePool")


	# Oranlar toplamı 100 olacak şekilde ayarlanmıştır. Örneğin, "Bait.png" %5, "ChillDog.png" %20, "ListeningMonkey.png" %20, "RelaxedDog.png" %20 ve "YouHaveBeenSaved.png" %35 oranlarına sahiptir.
	IMAGE_WEIGHTS = {
		"Bait.png": 5,
		"ChillDog.png": 20,
		"ListeningMonkey.png": 20,
		"RelaxedDog.png": 20,
		"YouHaveBeenSaved.png": 35
	}
	
	pygame.mixer.init()
	root, image_label, preloaded_images = setup_image_ui(IMAGE_DIR, IMAGE_WEIGHTS.keys())
	online_penceresi = create_online_overlay(root)

	listen = keyboard.Listener(on_release=on_release)
	listen.start()

	print("Sistem dinlemeye basladi")

	root.mainloop()