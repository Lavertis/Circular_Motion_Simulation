import pygame
import math


def draw(world):
    world.screen.fill((0, 0, 0))
    world.ball.display()
    world.circle.display_line(world.ball, world.surface_width, world.surface_height)
    display_frequency(world)
    display_fps(world)
    world.clock.tick(120)
    world.fps = world.clock.get_fps()
    pygame.display.flip()


def display_frequency(world):
    if world.ball_velocity_scale.get() == 0:
        text_surface = world.frequency_font.render('0 Hz', True, (120, 120, 120))
    else:
        frequency = 1 / (2 * math.pi / world.ball_velocity_scale.get())
        frequency = round(frequency, 2)
        text_surface = world.frequency_font.render(str(frequency) + ' Hz', True, (120, 120, 120))
    world.screen.blit(text_surface, (20, 20))


def display_fps(world):
    text_surface = world.fps_font.render('FPS: ' + str(round(world.fps)), True, (120, 120, 120))
    world.screen.blit(text_surface, (2, 0))
