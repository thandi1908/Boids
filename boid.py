# careful with naming the file and the class the same thing (not encountered in java)
from TwoVector import TwoVector as Vec
import pygame
from random import randrange


class Boid(object):

    def __init__(self, screen):
        self.position = Vec(randrange(500), randrange(500))
        self.velocity = Vec(randrange(-1, 1, 1), randrange(-1, 1, 1))
        self.image = pygame.image.load("icons8-triangle-96.png")
        self.screen = screen
        self.rect = self.image.get_rect()

    def blitme(self):
        """ Drawing the boid to the screen"""
        self.screen.blit(self.image, (self.position.x, self.position.y))

    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y


def spawn(screen):
    boid_list = []
    # creating 10 boids
    for i in range(10):
        boid = Boid(screen)
        boid_list.append(boid)
    return boid_list


def rule_one(boid_list):
    list_len = len(boid_list)
    new_pos = []
    for i in range(list_len):
        delta_x = 0
        delta_y = 0
        for j in range(list_len):
            if i != j:
                delta_x += boid_list[j].position.x / (list_len - 1)
                delta_y += boid_list[j].position.y / (list_len - 1)

        new_x = (boid_list[i].position.x - delta_x) / 1000
        new_y = (boid_list[i].position.y - delta_y) / 1000
        new_pos.append(Vec(boid_list[i].velocity.x - new_x, boid_list[i].velocity.y - new_y))
    for i in range(len(new_pos)):
        boid_list[i].velocity = new_pos[i]


def rule_two(boid_lis):
    ran = len(boid_lis)
    c_list = []
    for i in range(ran):
        zero = Vec(0, 0)
        for j in range(ran):
            if i != j:
                diff_pos = boid_lis[i].position.subtract(boid_lis[j].position)
                mod = diff_pos.dot_product(diff_pos)
                if mod**0.5 < 1000:
                    zero.subtract((boid_lis[i].position.subtract(boid_lis[j].position)))

        c_list.append(zero)
    for i in range(ran):
        boid_lis[i].velocity = boid_lis[i].velocity.subtract(c_list[i])



def rule_three(boid_list):
    list_len = len(boid_list)
    new_vel = []
    for i in range(list_len):
        delta_x = 0
        delta_y = 0
        for j in range(list_len):
            if i != j:
                delta_x += boid_list[j].velocity.x / (list_len - 1)
                delta_y += boid_list[j].velocity.y / (list_len - 1)

        new_x = (boid_list[i].velocity.x - delta_x) / 100
        new_y = (boid_list[i].velocity.y - delta_y) / 100
        new_vel.append(Vec(boid_list[i].velocity.x + new_x, boid_list[i].velocity.y + new_y))
    for i in range(len(new_vel)):
        boid_list[i].velocity = new_vel[i]

