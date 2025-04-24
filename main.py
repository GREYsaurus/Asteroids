# Import pygame for GUI functionalities
import pygame

# Import constants from constants.py
from constants import *

# Import classes from respective files
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot  # Import Shot class

def main():
    # Initialize pygame
    pygame.init()

    # Create a GUI window with the defined screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Clock object to manage frame rate
    clock = pygame.time.Clock()

    # Delta time variable, initialized to 0
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()  # For objects with an update method
    drawable = pygame.sprite.Group()  # For objects with a draw method
    asteroids = pygame.sprite.Group()  # For all asteroid objects
    shots = pygame.sprite.Group()  # Group for all bullet objects

    # Set containers for Player, AsteroidField, Asteroid, and Shot classes
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Asteroid.containers = asteroids, updatable, drawable
    Shot.containers = shots, updatable, drawable

    # Create the Player object and add it to the groups
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Create the AsteroidField object for spawning asteroids
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the loop if the window is closed

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update all objects in the updatable group
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Exit the program immediately if collision occurs

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()  # Remove the bullet
                    asteroid.split()  # Split the asteroid

        # Draw all objects in the drawable group
        for sprite in drawable:
            sprite.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()