import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("1000x1000")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        self.wall = Square(canvas=self.canvas, size=200, color="red", fill="red", line=2)
        self.wall.move_horizontal(50)
        self.wall.move_vertical(80)
        self.wall.make_visible()

        self.wall2 = Square(canvas=self.canvas, size=210, color="red", fill="red", line=2)
        self.wall2.move_horizontal(100)
        self.wall2.move_vertical(70)
        self.wall2.make_visible()

        self.grass = Square(canvas=self.canvas, size=800, color="green", fill="green", line=2)
        self.grass.move_horizontal(1)
        self.grass.move_vertical(200)
        self.grass.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="blue", fill="blue", line=1)
        self.window.move_horizontal(150)
        self.window.move_vertical(100)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="blue", fill="blue", line=1)
        self.window.move_horizontal(70)
        self.window.move_vertical(100)
        self.window.make_visible()

        self.window2 = Square(canvas=self.canvas, size=40, color="brown", fill="brown", line=1)
        self.window2.move_horizontal(50)
        self.window2.move_vertical(150)
        self.window2.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=75, width=175, color="brown", fill="brown", line=2)
        self.roof.move_horizontal(35)
        self.roof.move_vertical(113)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(200)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

        self.door = Rectangle(canvas=self.canvas, width=35, height=65, color="brown", fill="brown", line=1)
        self.door.move_horizontal(100)
        self.door.move_vertical(210)
        self.door.make_visible()
                        

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
