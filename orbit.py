import pygame
from pygame.math import Vector2
from math import sqrt
import sys
from sphere import Sphere
from typing import List

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

G = 6.673e-11

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# create the spheres
planet = Sphere(screen=screen, color=RED,pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), radius=50, velocity=(0, 0), mass = 1e17)
satelite = Sphere(screen=screen, color=GREEN,pos=(300, SCREEN_HEIGHT // 2), radius=20, velocity=(0, 0), mass = 1)
satelite.velocity = Vector2(0, sqrt(abs((G * planet.mass)/(satelite.pos.x - planet.pos.x))))

# create list of objects to compute gravitational force on each object
objects: List[Sphere] = []
objects.append(planet)
objects.append(satelite)

# Clock to control frame rate and measure time
clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(200) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # compute net force on each object
    for object in objects:
        x1 = object.pos
        m1 = object.mass
        print(x1)

        Fg = Vector2()

        # check every other object 
        for other_object in objects:
            if object is not other_object:
                # calculate the force of gravity
                m2 = other_object.mass
                x2 = other_object.pos
                r = (x2 - x1).magnitude()
                if r >= 1:
                  r_hat = (x2 - x1).normalize()
                  Fg += ((G*m1*m2)/(r**2))*r_hat
        
        print(f"Distance between objects: {(x2 - x1).x}")
        print(f"Force of gravity: {Fg.x}")
        object.pos = x1 + dt * object.velocity
        object.velocity = object.velocity + dt * (Fg/m1)

        object.draw()



    # command to update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
