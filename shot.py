import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS  # Import the shot radius constant

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Initialize the shot's position and radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt  # Update the shot's position