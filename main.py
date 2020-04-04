from tkinter import TclError

from world import *

world = World()

while world.loop:
    world.check_for_exit_and_window_resize()
    try:
        world.move_ball()
        world.draw()
        world.window.update()
    except TclError:
        break
world.exit()
