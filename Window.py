import sys
import pygame
from boid import spawn, rule_four
from boid import rule_one
from boid import rule_two
from boid import Boid

from boid import rule_three
from boid import Boid
from TwoVector import TwoVector as Vec
import time


def run_game():
    # Initialise game and create screen object
    screen_height = 700
    screen_width = 800
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Boids")
    screen.fill((0, 0, 0))
    boid_list = spawn(screen, 100)

    while True:
        # drawing the boids to the screen

        for obj in boid_list:
            obj.blitme()

        rule_one(boid_list)
        rule_two(boid_list)
        rule_three(boid_list)
        #rule_four(boid_list)

        for i in boid_list:
            i.wraparound(screen_width, screen_height)
            i.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = Boid(screen)
                click.position.x = pygame.mouse.get_pos()[0]
                click.position.y = pygame.mouse.get_pos()[1]

                boid_list.append(click)
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        screen.fill((0, 0, 0))


run_game()
