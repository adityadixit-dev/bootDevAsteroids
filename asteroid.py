import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        blue_angle = self.velocity.rotate(random_angle)
        red_angle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        blue_ast = Asteroid(self.position.x, self.position.y, new_radius)
        blue_ast.velocity = blue_angle * 1.2

        red_ast = Asteroid(self.position.x, self.position.y, new_radius)
        red_ast.velocity = red_angle * 1.2
