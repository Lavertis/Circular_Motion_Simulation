import math

import pygame


def check_for_exit_and_window_resize(world):
    for et in pygame.event.get():
        if et.type == pygame.QUIT:
            world.loop = False
        elif et.type == pygame.VIDEORESIZE:
            world.surface_size = et.size
            world.surface_width = et.w
            world.surface_height = et.h
            world.screen = pygame.display.set_mode(world.surface_size, pygame.RESIZABLE)


def move_ball(world):
    # Formulas for ball xy position from lecture
    # Half of the window width and height added in order to make the animation appear in the center
    world.ball.position.x = world.circle.radius * math.cos(world.circle.alpha) + world.surface_width / 2
    world.ball.position.y = world.circle.radius * math.sin(world.circle.alpha) + world.surface_height / 2
    if world.circle.alpha >= math.pi * 2:  # Check for passing full angle
        world.circle.alpha -= math.pi * 2  # Reset angle below 360°
    # App updates everything 'fps' times per second (method below ↓) so dividing 1 radian by 'fps' gives 1 radian
    # every one second which is then multiplied using the ball velocity control giving radians per second
    world.circle.alpha += 1 / world.fps * world.ball_velocity_scale.get()
    # 1 radian is 180° divided by π. π itworld is a 180° so π divided by π gives 1
