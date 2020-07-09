from action import *
from ball import *
from circle import *
from controls import *


class World(Controls):
    def __init__(self):
        super().__init__()
        # PyGame window
        pygame.init()
        pygame.display.set_caption("Circular motion")
        self.surface_height = round(0.75 * self.window.winfo_screenheight())
        self.surface_width = self.surface_height
        self.surface_size = (self.surface_width, self.surface_height)
        self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 10)
        self.loop = True
        self.frequency_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.ball = Ball(self.screen)
        self.circle = Circle(self.screen, self.surface_width, self.surface_height)
        self.initialize_fps_counter()
        # Controls window
        set_controls_commands(self)
        set_controls_defaults(self)

    def initialize_fps_counter(self):
        import time
        for _ in range(11):
            time.sleep(0.00001)
            self.clock.tick()
        move_ball(self)

    def exit(self):
        self.window.quit()
        pygame.quit()
