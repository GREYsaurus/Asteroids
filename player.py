import pygame
from circleshape import CircleShape
from shot import Shot  # Import the Shot class
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN  # Import constants

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initialize the rotation field
        self.shoot_timer = 0  # Timer to manage shooting cooldown

    # Method to calculate triangle vertices
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Override the draw method to display the triangle on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Method to rotate the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to move the player
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Method to shoot bullets
    def shoot(self):
        if self.shoot_timer > 0:
            return  # Prevent shooting if cooldown is active

        # Create a new shot at the player's current position
        shot = Shot(self.position.x, self.position.y)
        
        # Set the velocity based on the player's rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        # Reset the shoot timer
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    # Update method to handle movement, rotation, and shooting cooldown
    def update(self, dt):
        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            self.shoot_timer = max(self.shoot_timer, 0)  # Ensure it doesn't go below 0

        # Handle input for movement and shooting
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:  # Shoot bullets
            self.shoot()