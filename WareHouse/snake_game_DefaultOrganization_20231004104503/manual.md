# Snake Game User Manual

Welcome to the Snake Game user manual! This manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Table of Contents
1. [Installation](#installation)
2. [Main Functions](#main-functions)
3. [How to Play](#how-to-play)

## 1. Installation <a name="installation"></a>

To install the Snake Game, please follow the steps below:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the Snake Game source code from the provided files.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the Snake Game source code.

4. Create a virtual environment (optional but recommended) by running the following command:
   ```
   python -m venv snake-env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:
   - For Windows:
     ```
     snake-env\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source snake-env/bin/activate
     ```

6. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you are ready to play the Snake Game!

## 2. Main Functions <a name="main-functions"></a>

The Snake Game provides the following main functions:

- Snake movement: Use the arrow keys to control the snake's direction (up, down, left, right).
- Eating food: The snake can eat the red food to increase its score.
- Score display: The current score is displayed at the top left corner of the game window.
- Game over: The game ends if the snake collides with the wall or itself. The game over message is displayed in the center of the window.

## 3. How to Play <a name="how-to-play"></a>

To play the Snake Game, follow these steps:

1. Ensure that you have completed the installation steps mentioned in section 1.

2. Open a terminal or command prompt and navigate to the directory where you downloaded the Snake Game source code.

3. Activate the virtual environment (if you created one) by running the appropriate command mentioned in step 5 of the installation process.

4. Run the game by executing the following command:
   ```
   python main.py
   ```

5. The game window will appear, showing the snake and the food. Use the arrow keys to control the snake's movement and try to eat the food to increase your score.

6. Avoid colliding with the wall or the snake's own body. If the snake collides, the game will end, and the game over message will be displayed.

7. To play again, close the game window and repeat steps 4-6.

Enjoy playing the Snake Game!

If you have any questions or encounter any issues, please feel free to reach out to our support team for assistance.