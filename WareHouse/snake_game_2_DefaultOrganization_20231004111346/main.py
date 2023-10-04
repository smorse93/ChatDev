'''
This is the main file of the snake game.
'''
import pygame
import sys
from snake import Snake
from food import Food
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up the game clock
clock = pygame.time.Clock()
# Set up the game objects
snake = Snake(window_width, window_height)
food = Food(window_width, window_height)
# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update snake and food
    snake.update()
    snake.check_collision(food)
    # Clear the window
    window.fill((0, 0, 0))
    # Draw snake and food
    snake.draw(window)
    food.draw(window)
    # Update the display
    pygame.display.update()
    # Set the game speed
    clock.tick(10)
    # Add a delay
    pygame.time.delay(100)