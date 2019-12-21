import sys
import pygame
from boids.boid import spawn
from boids.boid import rule_one
from boids.boid import rule_two
from boids.boid import Boid

from boids.boid import rule_three
from boids.boid import Boid
from boids.TwoVector import TwoVector as Vec
import time


def run_game():
    # Initialise game and create screen object
    screen_height = 700
    screen_width = 800
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Boids")
    screen.fill((0, 0, 0))
    boid_list = spawn(screen)

    while True:
        # drawing the boids to the screen

        for obj in boid_list:
            obj.blitme()

        rule_one(boid_list)
        rule_two(boid_list)
        rule_three(boid_list)

        for i in boid_list:
            i.wraparound(screen_width,screen_height)
            i.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #time.sleep(0.01)
        pygame.display.flip()
        screen.fill((0, 0, 0))


run_game()
