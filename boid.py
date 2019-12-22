# careful with naming the file and the class the same thing (not encountered in java)
from TwoVector import TwoVector as Vec
import pygame
from random import randrange


class Boid(object):

    def __init__(self, screen):
        self.position = Vec(randrange(800), randrange(700))
        self.velocity = Vec(randrange(-2, 2, 1), randrange(-2, 2, 1))
        self.image = pygame.image.load("icons8-triangle-96.png")
        self.screen = screen
        self.rect = self.image.get_rect()

    def blitme(self):
        """ Drawing the boid to the screen"""
        self.screen.blit(self.image, (self.position.x, self.position.y))

    def update(self):
        pos = pygame.mouse.get_pos()

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    # Method from processing.org/flocking
    def wraparound(self, width, height):
        r = 2
        if self.position.x < -r:
            self.position.x = width + r
        if self.position.y < -r:
            self.position.y = height + r
        if self.position.x > width + r:
            self.position.x = -r
        if self.position.y > height + r:
            self.position.y = -r


def spawn(screen, number):
    boid_list = []
    # creating 10 boids
    for i in range(number):
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

        new_x = (boid_list[i].position.x - delta_x) / 300
        new_y = (boid_list[i].position.y - delta_y) / 300
        new_pos.append(Vec(new_x, new_y))

    for i in range(len(new_pos)):
        boid_list[i].velocity.x -= new_pos[i].x
        boid_list[i].velocity.y -= new_pos[i].y


def rule_two(boid_lis):
    ran = len(boid_lis)
    c_list = []
    for i in range(ran):
        zero = Vec(0, 0)
        for j in range(ran):
            if i != j:
                diff_pos = boid_lis[i].position.subtract(boid_lis[j].position)
                mod = diff_pos.dot_product(diff_pos)
                if mod < 1000:
                    diff = boid_lis[i].position.subtract(boid_lis[j].position)
                    zero = zero.subtract(diff)
                    zero = zero.scale(10)

        c_list.append(zero)

    for i in range(ran):
        boid_lis[i].velocity.x -= c_list[i].x
        boid_lis[i].velocity.y -= c_list[i].y


def rule_three(boid_list):
    list_len = len(boid_list)
    norm_len = list_len - 1
    new_vel = []
    for i in range(list_len):
        delta_x = 0
        delta_y = 0
        for j in range(list_len):
            if i != j:
                delta_x += boid_list[j].velocity.x / norm_len
                delta_y += boid_list[j].velocity.y / norm_len

        new_x = (boid_list[i].velocity.x - delta_x) / 8
        new_y = (boid_list[i].velocity.y - delta_y) / 8
        new_vel.append(Vec(new_x, new_y))

    for i in range(len(new_vel)):
        boid_list[i].velocity.x -= new_vel[i].x
        boid_list[i].velocity.y -= new_vel[i].y

def rule_four(boid_list):
    pos = pygame.mouse.get_pos()
    delta_x = []
    delta_y = []
    temp_x = 0
    temp_y = 0
    for i in boid_list:
        temp_x = i.position.x - pos[0]
        temp_y = i.position.y - pos[1]
        delta_x.append(temp_x)
        delta_y.append(temp_y)

    for i in range(len(boid_list)):
        boid_list[i].velocity.x -= delta_x[i]/100
        boid_list[i].velocity.y -= delta_y[i]/100

#def rule_five(list_boids):



