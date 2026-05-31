import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initialize screen and clock
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    

     # Calculate middle coordinates
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Instantiate the Player object in the center
    player = Player(x, y, PLAYER_RADIUS)

    while True:

        log_state()

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        dt = clock.tick(60) / 1000.0

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        print(f"Starting Asteroids with pygame version: {pygame.version.ver}! Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
