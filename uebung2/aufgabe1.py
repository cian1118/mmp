import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
sc_w = 1024
sc_h = 780
screen = pygame.display.set_mode((sc_w, sc_h), 0, 32)
pygame.display.set_caption("MMP - Übung 2")
back = pygame.Surface((sc_w, sc_h))
background = back.convert()
dark_blue = (51, 102, 255)
white = (255, 255, 255)
background.fill(dark_blue)

palm_med = pygame.image.load("palm.png").convert_alpha()  # 192x180
palm_sml = pygame.transform.scale(palm_med, (96, 90))
palm_lrg = pygame.transform.scale(palm_med, (240, 225))
boat = pygame.image.load("boat.png").convert_alpha()
boat_rect = boat.get_rect()
rect = boat.get_rect()


islands = [palm_lrg, palm_lrg, palm_med, palm_med, palm_sml]
rand_w = set()
rand_h = set()
while len(rand_w) < 5:
    rand_w.add(random.randrange(0, sc_w - palm_med.get_width(), palm_med.get_width()))
while len(rand_h) < 5:
    rand_h.add(random.randrange(0, sc_h - palm_med.get_height(), palm_med.get_height() / 2))
# blits 5 palm islands randomly on the screen, without overlapping
for x, y, i in zip(rand_w, rand_h, range(5)):
    background.blit(islands[i], (x, y))



boat_x, boat_y = sc_w/2, sc_h/2
mouse_x, mouse_y = boat_x, boat_y
speed = 3
boat_move = False
points = [(boat_x, boat_y)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            boat_move = True

    screen.blit(background, (0, 0))
    if boat_move:
        if mouse_x > boat_x:
            boat_x += speed
        if mouse_x < boat_x:
            boat_x -= speed
        if mouse_y > boat_y:
            boat_y += speed
        if mouse_y < boat_y:
            boat_y -= speed
        if (mouse_x == boat_x) and (mouse_y == boat_y):
            boat_move = False

        x_point = boat_x
        y_point = boat_y
        points.append((x_point, y_point))
        pygame.draw.lines(background, white, False, points)

    boat_centre_x = boat_x - boat_rect.w/2
    boat_centre_y = boat_y - (boat_rect.h/2)

    screen.blit(boat, (boat_centre_x, boat_centre_y))
    pygame.display.update()
