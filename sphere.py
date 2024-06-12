import pygame
from pygame.math import Vector2

RED = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Sphere:
    def __init__(
        self,
        screen: pygame.Surface,
        color: tuple[float, float, float],
        pos: tuple[float, float],
        radius: float,
        velocity: tuple[float, float],
        mass: float,
    ) -> None:
        self.screen = screen
        self.color = color
        self.pos = Vector2(pos)
        self.radius = radius
        self.mass = mass
        self.velocity = Vector2(velocity)


    def draw(self):
        pygame.draw.circle(
            surface=self.screen,
            color=self.color,
            center=self.pos,
            radius=self.radius,
        )
