import pygame
import random  # Import the random module
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS  # Import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # Method to split the asteroid
    def split(self):
        # Remove this asteroid
        self.kill()

        # Check if the asteroid is small enough to disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Do nothing if the asteroid is too small

        # Generate new smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create new velocity vectors for the split asteroids
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Rotate and scale
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Rotate opposite and scale

        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2