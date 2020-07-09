from draw import draw
from world import *

world = World()

while world.loop:
    check_for_exit_and_window_resize(world)
    try:
        draw(world)
        move_ball(world)
        world.window.update()
    except TclError:
        break
world.exit()
