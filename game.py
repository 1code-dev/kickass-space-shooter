#
# Step 1: Importing stuff
#


# Import the Pygame library
import pygame
import random  # Built in package for creating random values

# Initialize Pygame
# The `init()` function prepares Pygame for use.
pygame.init()

''' 
Note: `init` is short for "initialize",
which means to set up or prepare something for use.
'''


#
# Step 2: Creating constant values to be used later
#


# Creating some constant values,

''' 
Note: In python if we are creating some variable which should not be 
modified later on we name it in `all caps`, hence if a variable is 
constant name it in `all caps`.
'''

DISPLAY_WIDTH = 800  # For display width

DISPLAY_HEIGHT = 600  # For display height

WHITE_COLOR = (255, 255, 255)  # White color in RGB format

BLACK_COLOR = (0, 0, 0)  # Black color in RGB format

# Path to player img in asset
PLAYER_IMAGE = './projects-completed/assets/player.png'

# Path to enemy img in asset
ENEMY_IMAGE = './projects-completed/assets/enemy.png'

# Path to bullet img in asset
BULLET_IMAGE = './projects-completed/assets/bullet.png'

