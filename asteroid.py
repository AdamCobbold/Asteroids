from circleshape import CircleShape
import pygame # type: ignore
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_rad)
            new_ast2 = Asteroid(self.position.x, self.position.y, new_rad)
            new_ast1.velocity = vel1 * 1.2
            new_ast2.velocity = vel2 * 1.2
