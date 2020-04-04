from tkinter import Tk, Label, Scale, HORIZONTAL


class Controls:
    def __init__(self):
        self.window = Tk()
        self.set_window()
        # Ball velocity
        self.ball_velocity_label = Label(self.window)
        self.ball_velocity_scale = Scale(self.window)
        self.ball_velocity()
        # Ball radius
        self.ball_radius_label = Label(self.window)
        self.ball_radius_scale = Scale(self.window)
        self.ball_radius()
        # Ball colour
        self.circle_colour_label = Label(self.window)
        self.circle_colour_scale = Scale(self.window)
        self.ball_colour()
        # Circle radius
        self.circle_radius_label = Label(self.window)
        self.circle_radius_scale = Scale(self.window)
        self.circle_radius()
        # Circle radius colour
        self.circle_radius_colour_label = Label(self.window)
        self.circle_radius_colour_scale = Scale(self.window)
        self.circle_radius_colour()
        # Circle radius thickness
        self.circle_radius_thickness_label = Label(self.window)
        self.circle_radius_thickness_scale = Scale(self.window)
        self.circle_radius_thickness()
        self.pack()

    def set_window(self):
        window_size = str(round(self.window.winfo_screenwidth() * 0.18)) + 'x' + str(
            round(self.window.winfo_screenheight() * 0.77)) + '+' + str(
            round(self.window.winfo_screenwidth() * 0.75)) + '+' + str(
            round(self.window.winfo_screenheight() * 0.096))
        self.window.geometry(window_size)
        self.window.resizable(0, 0)
        self.window.attributes('-topmost', True)
        self.window.title("Controls")

    def ball_velocity(self):
        self.ball_velocity_label.config(text="\nAngular velocity [rad/s]", font=("Arial", 14))
        self.ball_velocity_scale.config(length=260, width=25, sliderlength=60, from_=0, to=10, resolution=0.1,
                                        orient=HORIZONTAL)

    def ball_radius(self):
        self.ball_radius_label.config(text="\nBall radius", font=("Arial", 14))
        self.ball_radius_scale.config(length=260, width=25, sliderlength=60, from_=10, to=150, orient=HORIZONTAL)

    def ball_colour(self):
        self.circle_colour_label.config(text="\nBall colour", font=("Arial", 14))
        self.circle_colour_scale.config(length=260, width=25, sliderlength=60, from_=1, to=7, resolution=1,
                                        orient=HORIZONTAL)

    def circle_radius(self):
        self.circle_radius_label.config(text="\nCircle radius", font=("Arial", 14))
        self.circle_radius_scale.config(length=260, width=25, sliderlength=60, from_=30, to=450, resolution=1,
                                        orient=HORIZONTAL)

    def circle_radius_colour(self):
        self.circle_radius_colour_label.config(text="\nRadius colour", font=("Arial", 14))
        self.circle_radius_colour_scale.config(length=260, width=25, sliderlength=60, from_=1, to=7, resolution=1,
                                               orient=HORIZONTAL)

    def circle_radius_thickness(self):
        self.circle_radius_thickness_label.config(text="\nRadius thickness", font=("Arial", 14))
        self.circle_radius_thickness_scale.config(length=260, width=25, sliderlength=60, from_=1, to=5, resolution=1,
                                                  orient=HORIZONTAL)

    def pack(self):
        self.ball_velocity_label.pack()
        self.ball_velocity_scale.pack()
        self.ball_radius_label.pack()
        self.ball_radius_scale.pack()
        self.circle_colour_label.pack()
        self.circle_colour_scale.pack()
        self.circle_radius_label.pack()
        self.circle_radius_scale.pack()
        self.circle_radius_colour_label.pack()
        self.circle_radius_colour_scale.pack()
        self.circle_radius_thickness_label.pack()
        self.circle_radius_thickness_scale.pack()
