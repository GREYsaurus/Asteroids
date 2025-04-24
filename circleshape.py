import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # We will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass

    def collides_with(self, other):
    # Calculate the distance between this CircleShape and another
        distance = self.position.distance_to(other.position)
    # Return True if the distance is less than the combined radii (collision)
        return distance < self.radius + other.radius