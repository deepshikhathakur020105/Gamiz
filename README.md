# Gamiz
# Ultimate Mystery Quiz

## Overview
The "Ultimate Mystery Quiz" is a fun and interactive quiz game built using Python and Tkinter. It features a series of mysterious questions and engaging sound effects. Additionally, it includes two mini-games: a Number Guessing Game and Rock-Paper-Scissors.

## Features
- Multiple-choice quiz with progress tracking
- Sound effects for button clicks and results
- Mini-games for additional fun
- Dark-themed UI

## Requirements
- Python 3.x
- Required Python libraries:
  ```sh
  pip install pygame
  ```
- Ensure `click.wav` and `win.wav` exist in the directory (optional for sound effects)

## Running the Application
Run the following command in the terminal:
```sh
python quiz.py
```

---

# Creating an Installer with Inno Setup
To distribute the application as an executable, we use **Inno Setup**.

## Steps to Create an Installer

1. **Convert Python Script to Executable**
   - Install `pyinstaller`:
     ```sh
     pip install pyinstaller
     ```
   - Convert the script:
     ```sh
     pyinstaller --onefile --windowed --icon=icon.ico quiz.py
     ```
   - The `.exe` file will be in the `dist/` folder.

2. **Install Inno Setup**
   - Download and install [Inno Setup](https://jrsoftware.org/isinfo.php).

3. **Create an Inno Setup Script (`setup.iss`)**
   ```iss
   [Setup]
   AppName=Ultimate Mystery Quiz
   AppVersion=1.0
   DefaultDirName={pf}\UltimateMysteryQuiz
   OutputDir=.
   OutputBaseFilename=UltimateMysteryQuizSetup
   Compression=lzma
   SolidCompression=yes

   [Files]
   Source: "dist\quiz.exe"; DestDir: "{app}"; Flags: ignoreversion

   [Icons]
   Name: "{group}\Ultimate Mystery Quiz"; Filename: "{app}\quiz.exe"
   Name: "{userdesktop}\Ultimate Mystery Quiz"; Filename: "{app}\quiz.exe"

   [Run]
   Filename: "{app}\quiz.exe"; Description: "Launch Ultimate Mystery Quiz"; Flags: nowait postinstall
   ```

4. **Compile the Script**
   - Open Inno Setup Compiler
   - Load `setup.iss`
   - Click **Compile**

5. **Installer is Ready!**
   - The installer `.exe` will be generated in the specified Output Directory.
   - Run it to install the game on any Windows PC.

---
## Installation

1. **Download the Setup**

   [![Download ](https://img.shields.io/badge/Download-Setup-green?style=for-the-badge)](<https://drive.google.com/file/d/1Q3YDrWn-Xlh_30ObM7fp5UHG-vDPy3dj/view?usp=sharing>)

2. **Extract and Run**
   - Extract the downloaded file.
   - Run `setup.exe` (Windows) or `python main.py` (for manual execution).


## License
MIT License

