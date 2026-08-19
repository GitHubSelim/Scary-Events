# Getting Started

## ScaryEvents - Setup Guide 💡

Welcome, this guide will walk you through running the **ScaryEvents** project step-by-step. Even if you're new to Python or programming. No experience needed.

---

[🔀Changing the app that gets muted](#changing-the-app-that-gets-muted)

###  1. Download the Project ZIP

> ✅ The code is **portable**, meaning it works directly from the downloaded folder.

1. Go to the GitHub repo (example):\
[https://github.com/GitHubSelim/Scary-Events](https://github.com/GitHubSelim/Scary-Events)

3. Click the green **Code** button → **Download ZIP**

4. Extract the `.zip` file to your desktop or a folder of your choice.


### B. Clone via Git (Optional, if you prefer Git over ZIP:)
> Remember you need to have [git](https://git-scm.com/downloads) installed 
If you prefer using the terminal:
```bash
git clone https://github.com/GitHubSelim/Scary-Events.git
cd ScaryEvents
```
---
### 🐍 2. Install Python (if you haven’t)

> Skip this step if you already have Python installed.

1. Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download **Python 3.7** or higher
3.  On the installer screen, make sure to **check** the box:\
    “Add Python to PATH”
4. Finish the install

---

###  3. Install Required Libraries


1. Open the folder where you extracted the project

2. In the white area of the folder, **hold Shift** + **Right-click**, then choose:\
**“Open PowerShell window here” (or "Open Terminal" on newer Windows)**

3. Paste this command and hit **Enter**:

```bash
pip install pillow pynput pycaw comtypes
```

That’s it! 

---

### ▶️ 4. Run main.py

This will wait for you to press the `"-" key`

1. In the same terminal, type:

```bash
python main.py
```

2. Wait until an **Online** text pops on upper-right corner of your screen. This means the script has finished loading.
3. The program waits for `"-" key` → then it displays a random image ,selected from ImagePool, on top of your current screen.
4. To close the image just press `Enter`
5. Exit the script by pressing to the `ESC` key.


>The script never exits until you press the `ESC` key. So you can avoid multiple jumpscares by pressing the "-" key.


---

### 🔀 Changing the app that gets muted


When you run main.py, a folder named "assets" gets created if there isn't one. 
Inside it you should see a txt file named: "processes.txt".



1. After you found the txt file, you should write the process names of the apps that you want to mute into the text file.
    >Usually the process names are the "name of the app" + ".exe". 
    >>For instance, chrome.exe, brave.exe


    Eg. processes.txt:
    ```text
    chrome.exe
    brave.exe
    ```
    You can find the process names by opening the Task Manager on Windows and opening the tab named "Processes".

2. Finally save the text file.


- Note: If you don't change the processes.txt file, the default game that gets muted is Escape the Backrooms -not affiliated-.

---

### 🧐 What’s Next?

You can now:

- Peacefully listen to a music with a nice image when a jumpscare happens.
- Be aware of the surrondings even if a jummpscare occurs. (The only apps that gets muted are the ones written in the processes.txt file)

---

### 💬 Need Help?

If you have trouble:

- Open an issue on GitHub
- Or contact me at: `projects.selim@gmail.com`

---

> Don’t just learn it; break, fix, then reinvent it.