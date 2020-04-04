import os

from ball import *
from circle import *
from controls import *


class World(Controls):
    def __init__(self):
        if os.name == 'nt':
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        super().__init__()
        # Pygame window
        pygame.init()
        pygame.display.set_caption("Circular motion")
        self.surface_height = round(0.75 * self.window.winfo_screenheight())
        self.surface_width = self.surface_height
        self.surface_size = [self.surface_width, self.surface_height]
        self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = self.initialize_fps_counter()
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 10)
        self.loop = True
        self.frequency_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.ball = self.create_ball()
        self.circle = self.create_circle()
        # Controls window
        self.set_controls_commands()
        self.set_controls_defaults()

    def initialize_fps_counter(self):
        for _ in range(11):
            self.clock.tick()
        return self.clock.get_fps()

    def create_ball(self):
        return Ball(surface=self.screen)

    def create_circle(self):
        return Circle(surface=self.screen, surface_width=self.surface_width, surface_height=self.surface_height)

    def set_controls_commands(self):
        self.ball_velocity_scale.config(command=self.ball.change_velocity)
        self.ball_radius_scale.config(command=self.ball.change_radius)
        self.circle_colour_scale.config(command=self.ball.change_colour)
        self.circle_radius_scale.config(command=self.circle.change_radius)
        self.circle_radius_colour_scale.config(command=self.circle.change_radius_line_colour)
        self.circle_radius_thickness_scale.config(command=self.circle.change_radius_line_thickness)

    def set_controls_defaults(self):
        self.ball_velocity_scale.set(self.ball.velocity)
        self.ball_radius_scale.set(self.ball.radius)
        self.circle_colour_scale.set(self.ball.colours.index(self.ball.colour_name) + 1)
        self.circle_radius_scale.set(self.circle.radius)
        self.circle_radius_colour_scale.set(self.circle.colours.index(self.circle.colour_name) + 1)
        self.circle_radius_thickness_scale.set(self.circle.radius_line_thickness)

    def check_for_exit_and_window_resize(self):
        for et in pygame.event.get():
            if et.type == pygame.QUIT:
                self.loop = False
            elif et.type == pygame.VIDEORESIZE:
                self.surface_size = et.size
                self.surface_width = et.w
                self.surface_height = et.h
                self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)

    def move_ball(self):
        # Formulas for ball xy position from lecture
        # Half of the window width and height added in order to make the animation appear in the center
        self.ball.position.x = self.circle.radius * math.cos(self.circle.alpha) + self.surface_width / 2
        self.ball.position.y = self.circle.radius * math.sin(self.circle.alpha) + self.surface_height / 2
        if self.circle.alpha >= math.pi * 2:  # Check for passing full angle
            self.circle.alpha -= math.pi * 2  # Reset angle below 360°
        # App updates everything 'fps' times per second (method below ↓) so dividing 1 radian by 'fps' gives 1 radian
        # every one second which is then multiplied using the ball velocity control giving radians per second
        self.circle.alpha += 1 / self.fps * self.ball_velocity_scale.get()
        # 1 radian is 180° divided by π. π itself is a 180° so π divided by π gives 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ball.display()
        self.circle.display_line(self.ball, self.surface_width, self.surface_height)
        self.display_frequency()
        self.display_fps()
        self.clock.tick(240)
        self.fps = self.clock.get_fps()
        pygame.display.flip()

    def display_frequency(self):
        if self.ball_velocity_scale.get() == 0:
            text_surface = self.frequency_font.render('0 Hz', True, (120, 120, 120))
        else:
            frequency = 1 / (2 * math.pi / self.ball_velocity_scale.get())
            frequency = round(frequency, 2)
            text_surface = self.frequency_font.render(str(frequency) + ' Hz', True, (120, 120, 120))
        self.screen.blit(text_surface, (20, 20))

    def display_fps(self):
        if self.fps == math.inf:
            text_surface = self.fps_font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.fps_font.render('FPS: ' + str(round(self.fps)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 0))

    def exit(self):
        import sys
        self.window.quit()
        pygame.quit()
        sys.exit()
