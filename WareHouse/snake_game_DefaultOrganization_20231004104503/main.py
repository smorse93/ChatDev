'''
This is the main file of the snake game application.
'''
import tkinter as tk
from snake import SnakeGame
def main():
    root = tk.Tk()
    root.title("Snake Game")
    game = SnakeGame(root)
    game.pack()
    root.mainloop()
if __name__ == "__main__":
    main()