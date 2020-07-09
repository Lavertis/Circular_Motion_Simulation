import pygame


class Ball:
    def __init__(self, surface):
        self.surface = surface
        self.velocity = 1
        self.radius = 50
        self.diameter = 2 * self.radius
        self.colour_name = 'blue'
        self.colours = ['red', 'green', 'blue', 'white', 'orange', 'yellow', 'purple']
        self.colour = pygame.color.Color(self.colour_name)
        self.position = pygame.Vector2()

    def display(self):
        pygame.draw.ellipse(self.surface, self.colour, (
            self.position.x - self.radius, self.position.y - self.radius, self.diameter, self.diameter))

    def change_velocity(self, value):
        self.velocity = value

    def change_radius(self, value):
        self.radius = int(value)
        self.diameter = 2 * self.radius

    def change_colour(self, value):
        self.colour = pygame.color.Color(self.colours[int(value) - 1])
        self.colour_name = self.colours[int(value) - 1]
