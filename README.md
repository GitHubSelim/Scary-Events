<p align="center">
<img src="./assets/ScaryEvents.png" width="400" />
</p>v

# ScaryEvents

ScaryEvents is a Python project for managing in-game jumpscares.  
It listens for the keyboard, specifically the "-" key, projects instant visuals onto the screen, mutes the main game audio, and plays a relaxing audio (`.mp3`) file in the background.  

The project is built with a modular architecture and compiled into a standalone executable.

## 📌 Overview

The project consists of **three main components**:

### 👻 Main.py
* Mutes the system/game audio when a trigger occurs.  
* Projects visual assets over the game screen.  
* Plays a background `.mp3` audio file simultaneously.  

### 💽 Media Loader
* Reads images and audio dynamically from an external folder named `resimhavuzu`.  
* Allows easy replacement of jumpscare media without editing or recompiling the code.  

### 🚀 Standalone Executable
* Bundled using `PyInstaller` for end-users.  
* Requires **no Python installation** or environment setup to run.  

---

## 📁 Project Structure

```text
ScaryEvents/
│   main.py                      # The entry point script that initializes the application and coordinates the other modules.
│   audio_manager.py             # Handles the muting of the main system audio and the playback of custom audio files.
│   image_selector.py            # Dynamically chooses which visual asset to display from the directory during an event.
│   load_image.py                # Responsible for reading and preparing the selected image files for rendering.
│   overlay_manager.py           # Manages the on-screen "ONLINE "display, rendering text on top of the active game window showing the script is running at that moment.
│   LICENSE                      # GPLv3 license text file detailing usage rights.
|
└──assets/                    # Directory storing all media elements like jumpscare images and audio.
      |
      ├──ImagePool/                  # External folder for media assets
      |
      |      Bait.png                         # Visual files
      |      ChillDog.png                     # Visual files
      |      ListeningMonkey.png              # Visual files
      |      RelaxedDog.png                   # Visual files
      |      YouHaveBeenSaved.png             # Visual files
      |    Grieg - Morning Mood(flute).mp3  # audio file
```

---

## 🛠️ Prerequisites

* **Python:** 3.7 or higher
* **Optional:** [Anaconda](https://www.anaconda.com/) (for easier environment management)   
* **Libraries used:**
  - `pillow`   – external library (install via pip)
  - `pynput`   – external library (install via pip)
  - `pycaw`   – external library (install via pip)
  - `comtypes`   – external library (install via pip)
  - `tkinter`  – standard library (GUI support; usually bundled with Python)
  -
   
  - Built-in modules: `os`, `sys`, `random` and `pygame`

Install dependencies via **pip**:

```bash
pip install pillow pynput pycaw comtypes
```

Or using **conda**:

```bash
conda create -n ScaryEvents python=3.11
conda activate ScaryEvents
pip install pillow pynput pycaw comtypes
```

---

## 🚀 Cross-Platform Notes

* Fully tested on **Windows 10/11**.  
* The compiled `.exe` version in the Releases tab is specifically designed for Windows environments.  
* If running from the source code (`.py`), requires manual execution via terminal.  

---

### 📖 Need help getting started?

You don't need to touch the code to use the application!  
➡️ **Download the ready-to-use executable from the [Releases](../../releases) tab.**

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. 
The source code of the project must remain open; if copied or modified, the original attribution must be preserved, and it must be distributed under the same license. For commercial use terms and further details, please refer to the `LICENSE` file.

---
**Copyright (c) 2026 Ahmet Selim GÜNGÖR**