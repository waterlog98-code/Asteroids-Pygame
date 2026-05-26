import pygame
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    # Initialize screen and clock
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

     # Calculate middle coordinates
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Instantiate the Player object in the center
    player = Player(x, y, PLAYER_RADIUS)

    while True:
        log_state()
        screen.fill("black")
        player.draw(screen)
        
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        print(f"Starting Asteroids with pygame version: {pygame.version.ver}! Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
