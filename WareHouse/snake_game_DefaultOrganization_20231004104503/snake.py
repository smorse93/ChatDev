'''
This file contains the SnakeGame class which represents the snake game.
'''
import tkinter as tk
import random
class SnakeGame(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=600, height=400, background="black", highlightthickness=0)
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.create_food()
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)
        self.score = 0
        self.score_text = self.create_text(50, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 14), anchor="nw")
        self.speed = 100
        self.move_snake()
    def create_food(self):
        x = random.randint(1, 29) * 20
        y = random.randint(1, 19) * 20
        return self.create_oval(x, y, x+20, y+20, fill="red")
    def move_snake(self):
        head_x, head_y = self.snake_positions[0]
        if self.direction == "Right":
            new_head = (head_x + 20, head_y)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)
        self.snake_positions.insert(0, new_head)
        if self.check_collision():
            self.game_over()
            return
        if new_head == self.food_position:
            self.score += 1
            self.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.delete(self.food_position)
            self.food_position = self.create_food()
        else:
            self.snake_positions.pop()
        self.delete(tk.ALL)
        for position in self.snake_positions:
            self.create_rectangle(position[0], position[1], position[0]+20, position[1]+20, fill="green")
        self.create_oval(self.food_position, fill="red")
        self.after(self.speed, self.move_snake)
    def check_collision(self):
        head_x, head_y = self.snake_positions[0]
        return (
            head_x < 0 or
            head_x >= 600 or
            head_y < 0 or
            head_y >= 400 or
            (head_x, head_y) in self.snake_positions[1:]
        )
    def game_over(self):
        self.delete(tk.ALL)
        self.create_text(300, 200, text="Game Over", fill="white", font=("Arial", 24), anchor="center")
    def on_key_press(self, event):
        keysym = event.keysym
        if keysym == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif keysym == "Down" and self.direction != "Up":
            self.direction = "Down"