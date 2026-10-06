# Byte Brawl - a 2D Combat Game (Python)
This is a 2D fighting game built using Pygame. The game features two playable characters who can move, jump, attack, and engage in a fight.
The player controls are mapped to the keyboard, and the game includes sprite-based animation for actions such as walking, attacking, and taking damage.
The fight ends when one player's health reaches zero, the winner is announced, and a menu lets the players restart the fight or exit the game.
## Download and Play (no Python needed)
Ready-to-play builds are available on the [Releases page](https://github.com/avi-saraiya/Byte-Brawl/releases/latest).
* <b>Windows 10/11 (64-bit):</b> Download `ByteBrawl.exe` and double-click it. If Windows SmartScreen shows "Windows protected your PC", click <i>More info</i> → <i>Run anyway</i>.
* <b>Linux (x86-64):</b> Download `ByteBrawl-linux`, then run `chmod +x ByteBrawl-linux` and `./ByteBrawl-linux`.
## Features
* <b>Two Player Mode:</b> Control two fighters, each with distinct movement and attack animations.
* <b>Character Animations:</b> Sprite-based animations for attacking, idle, running, and taking damage.
* <b>Health Bar:</b> Displays the current health for both players, which depletes when hit.
* <b>Movement and Combat:</b> Players can move left, right, jump, and attack.
* <b>End-of-Fight Menu:</b> When a player's health reaches zero, the winner is announced and a menu appears with Restart and Exit options.
* <b>Standalone Builds:</b> Packaged with PyInstaller into single-file executables for Windows and Linux.
## Requirements (running from source)
* Python 3.x
* pygame-ce (the community edition of Pygame)
* PyInstaller (only needed to build the executables)
## Installing Dependencies
From the `byte_brawl` folder, install everything with pip:
```
pip install -r requirements.txt
```
## File Structure
```
byte_brawl/
├── assets/
│   ├── background_image.png
│   ├── MartialHero.png
│   └── EvilWizard.png
├── pyfiles/
│   ├── fighter.py
│   └── main.py
├── ByteBrawl.spec
└── requirements.txt
```
### assets
Contains the necessary assets like images for the background and character sprites.
### fighter.py
Defines the Fighter class which handles the logic for each fighter, including movement, attack, animation, and health management.
### main.py
The main game loop, where the players' actions are processed, animations are displayed, the health bar is updated, and the end-of-fight menu is shown.
### ByteBrawl.spec
The PyInstaller build configuration used to package the game into a single executable.
### requirements.txt
Lists the Python packages needed to run and build the game.
## Game Controls
### Player 1 (Martial Hero)
* Move Left: A
* Move Right: D
* Jump: W
* Attack: S
### Player 2 (Evil Wizard)
* Move Left: J
* Move Right: L
* Jump: I
* Attack: K
### End-of-Fight Menu
* Select: Mouse, W/S, or the Up/Down arrow keys
* Confirm: Left click, Enter, or Space
## How to Play
<b>Start the Game:</b><br><br> When the game begins, a countdown appears, and once it hits "Fight!", the match starts.<br>
<br>
<b>Control your Fighter:</b><br><br> Use the keyboard controls to move, jump, and attack your opponent.<br>
<br>
![battle_game 2024-12-20 11_28_08 AM](https://github.com/user-attachments/assets/b5d0fdfc-d074-4177-bc51-982e218e8bb5)
<br>
![battle_game 2024-12-20 11_29_12 AM](https://github.com/user-attachments/assets/f5b3fc81-4e8b-4de8-a812-74f7666beaee)
<br>
![battle_game 2024-12-20 11_30_35 AM](https://github.com/user-attachments/assets/9ab2ad12-2b2a-427d-82fe-dfcd60c6733a)
<br><br>
<b>Winning:</b><br><br> The fight ends when one player's health reaches zero. The winner is displayed on the screen.<br>
<br>
![battle_game 2024-12-20 11_31_19 AM](https://github.com/user-attachments/assets/71860a1a-33ac-4295-885c-ab682de797d9)
<br><br>
<b>Restart or Exit:</b><br><br> Shortly after the winner is announced, a menu appears. Choose <i>Restart</i> to start a fresh fight with full health, or <i>Exit</i> to close the game.<br>
## Code Explanation
### Fighter Class (fighter.py)
The Fighter Class defines the core logic for each fighter, including:<br>
* <b>Movement:</b> Players can move left and right using the respective controls.
* <b>Attack:</b> Players can attack by pressing the attack button, which decreases the opponent's health.
* <b>Jump:</b> Fighters can jump when the jump button is pressed.
* <b>Animation:</b> Each action (attack, idle, running, hit) is represented by different frames, which are shown in sequence.
* <b>Health Management:</b> Each player has a health bar that decreases when they are hit by an attack.
### Main Class (main.py)
* <b>Game Setup</b>: The screen, background, and sprite images are initialized. Images are loaded through `resource_path()`, so the game finds its assets whether it runs from source or from a packaged executable.
* <b>Countdown:</b> A countdown is shown at the start before the players can start moving.
* <b>Game Loop:</b> The main loop handles drawing the background, updating the players’ positions and animations, and checking for collisions (attacks).
* <b>Health Bars:</b> Each player's health is displayed on top of the screen, which decreases when they take damage.
* <b>End Game:</b> When one player's health reaches zero, the game displays a message declaring the winner (or a draw if both fall at once), then shows the Restart/Exit menu.
* <b>Restart:</b> `reset_game()` creates fresh fighters and restarts the countdown, so every fight starts from the same state.
## How to Run the Game from Source
Clone the repository
```
git clone https://github.com/avi-saraiya/Byte-Brawl.git
```
Navigate to the game folder
```
cd Byte-Brawl/byte_brawl
```
Install the dependencies
```
pip install -r requirements.txt
```
Finally, run the main.py file
```
python pyfiles/main.py
```
## Building the Executable
From the `byte_brawl` folder, run:
```
pyinstaller ByteBrawl.spec
```
The executable is created in the `dist` folder. PyInstaller builds for the operating system it runs on, so build on Windows to get `ByteBrawl.exe` and on Linux to get the Linux version.
## Notes
* You may add your own sprite images and background images to the assets folder if you want to.
* The game runs at 70 frames per second and supports two players on the same keyboard.
## Credits
Coding with Russ (Youtube)<br>
luizmelo.itch.io
