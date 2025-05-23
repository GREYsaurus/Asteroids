import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Asteroid.containers = asteroids, updatable, drawable
    Shot.containers = shots, updatable, drawable
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    # Initialize score
    score = 0
    font = pygame.font.Font(None, 36)  # Default font, size 36

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 10  # Increment score when an asteroid is destroyed

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Render the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Draw score at the top-left corner

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()