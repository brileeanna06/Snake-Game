import pygame as pg
import random

# Colors
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
brown = pg.Color(165, 42, 42)
# Variables
screen_width = 400
screen_height = 400


# The class for food object
class Food:
    # Initialization
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 4
        self.color = red
        self.width = 10
        self.height = 10

    # Makes the food visible
    def draw_food(self, surface):
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.color, self.food)

    # Is the food eaten?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Returns a new position for the food after it is eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
