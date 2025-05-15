import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for u in updatable:
            u.update(dt)

        for ast in asteroids:
            if ast.is_colliding_with(player):
                print("Game Over")
                sys.exit()

            for s in shots:
                if ast.is_colliding_with(s):
                    s.kill()
                    ast.split()

        for d in drawable:
            d.draw(screen)

        # display flip should be last
        pygame.display.flip()
        dt = py_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
