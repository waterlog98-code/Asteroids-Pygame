from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> list["Asteroid"]:
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []

        log_event("asteroid_split")
        angle1 = random.uniform(-50, -20)
        angle2 = random.uniform(20, 50)

        speed = self.velocity.length() or 100
        v1 = pygame.math.Vector2(1, 0).rotate(angle1) * speed
        v2 = pygame.math.Vector2(1, 0).rotate(angle2) * speed

        child_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, child_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, child_radius)
        asteroid1.velocity = v1
        asteroid2.velocity = v2
        self.kill()

        return [asteroid1, asteroid2]