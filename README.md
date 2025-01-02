# Byte Brawl - a 2D Combat Game (Python)
This is a 2D fighting game built using Pygame. The game features two playable characters who can move, jump, attack, and engage in a fight.
The player controls are mapped to the keyboard, and the game includes sprite-based animation for actions such as walking, attacking, and taking damage.
The game ends when one player's health reaches zero, and the winner is announced.
## Features
* <b>Two Player Mode:</b> Control two fighters, each with distinct movement and attack animations.
* <b>Character Animations:</b> Sprite-based animations for attacking, idle, running, and taking damage.
* <b>Health Bar:</b> Displays the current health for both players, which depletes when hit.
* <b>Movement and Combat:</b> Players can move left, right, jump, and attack.
* <b>Game Over State:</b> The game ends when a player's health reaches zero.
## Requirements
* Python 3.x
* Pygame library
## Installing Pygame
To install the Pygame library, you can use pip:<br>
<br>
![image](https://github.com/user-attachments/assets/ec08e481-e0ca-4bdb-84ec-7107f7e68e2c)
<br>
## File Structure
![image](https://github.com/user-attachments/assets/1fcf2dd8-bfce-43a3-a736-53c31e797b5c)<br>
### assets
Contains the necessary assets like images for the background and character sprites.
### fighter.py
Defines the Fighter class which handles the logic for each fighter, including movement, attack, animation, and health management.
### main.py
The main game loop, where the players' actions are processed, animations are displayed, and the health bar is updated.
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
## How to Play
<b>Start the Game:</b><br><br> When the game begins, a countdown appears, and once it hits "Fight!", the match starts.<br>
<br>
ADD IMAGE HERE <br><br>
<b>Control your Fighter:</b><br><br> Use the keyboard controls to move, jump, and attack your opponent.<br>
<br>
ADD IMAGE HERE<br><br>
<b>Winning:</b><br><br> The game ends when one player's health reaches zero. The winner is displayed on the screen.<br>
<br>
ADD IMAGE HERE<br>
## Code Explanation
### Fighter Class (fighter.py)
The Fighter Class defines the core logic for each fighter, including:<br>
* <b>Movement:</b> Players can move left and right using the respective controls.
* <b>Attack:</b> Players can attack by pressing the attack button, which decreases the opponent's health.
* <b>Jump:</b> Fighters can jump when the jump button is pressed.
* <b>Animation:</b> Each action (attack, idle, running, hit) is represented by different frames, which are shown in sequence.
* <b>Health Management:</b> Each player has a health bar that decreases when they are hit by an attack.
### Main Class (main.py)
* <b>Game Setup</b>: The screen, background, and sprite images are initialized.
* <b>Countdown:</b> A countdown is shown at the start before the players can start moving.
* <b>Game Loop:</b> The main loop handles drawing the background, updating the players’ positions and animations, and checking for collisions (attacks).
* <b>Health Bars:</b> Each player's health is displayed on top of the screen, which decreases when they take damage.
* <b>End Game:</b> When one player's health reaches zero, the game displays a message declaring the winner.
## How to Run the Game
Clone the repository<br>
<br>
ADD IMAGE HERE<br><br>
Navigate to the game folder<br>
<br>
ADD IMAGE HERE<br><br>
Run the game<br>
<br>
ADD IMAGE HERE<br>
## Notes
* You may need to add your own sprite images and background images to the assets/ folder.
* The game runs at 70 frames per second and supports two players on the same keyboard.
## License
This project is open-source and available under the MIT License.
