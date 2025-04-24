# Import pygame for GUI functionalities
import pygame

# Import constants from constants.py
from constants import *

def main():
    # Initialize pygame (required for using its features)
    pygame.init()

    # Create a GUI window with the defined screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite game loop
    while True:
        # Check for events (e.g., if the user closes the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the loop if the window is closed

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()