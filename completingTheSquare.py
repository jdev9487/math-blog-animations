from manim import *
import numpy as np

class Source(Scene):
    def construct(self):
        gap = 0.1
        rect_width = 0.7
        c_width = 1.7
        x_squared = Square(2, color=RED)
        rect1 = Rectangle(height=2, width=0.7, color=GREEN).shift(RIGHT * (1 + gap + rect_width/2))
        rect2 = Rectangle(height=2, width=0.7, color=GREEN).shift(RIGHT * (1 + 2*gap + 3*rect_width/2))
        completer = Square(rect_width).shift((RIGHT+UP)*(1 + gap + rect_width/2))
        unadjustedPoints = [
            [5-c_width/2, 1.5-c_width/2, 0],
            [5+c_width/2, 1.5-c_width/2, 0],
            [5+c_width/2, 1.5+c_width/2, 0],
            [5-c_width/2+rect_width, 1.5+c_width/2, 0],
            [5-c_width/2, 1.5+c_width/2, 0],
            [5-c_width/2, 1.5+c_width/2-rect_width, 0]
        ]
        adjustedPoints = [
            [5-c_width/2, 1.5-c_width/2, 0],
            [5+c_width/2, 1.5-c_width/2, 0],
            [5+c_width/2, 1.5+c_width/2, 0],
            [5-c_width/2+rect_width, 1.5+c_width/2, 0],
            [5-c_width/2+rect_width, 1.5+c_width/2-rect_width, 0],
            [5-c_width/2, 1.5+c_width/2-rect_width, 0]
        ]
        c = Polygon(*unadjustedPoints)
        adjusted = Polygon(*adjustedPoints, color=PINK)
        self.play(Create(x_squared))
        self.play(Create(rect1))
        self.play(Create(rect2))
        self.play(Create(c))
        self.wait()
        self.play(Rotate(rect1, angle=PI/2, about_point=ORIGIN), rect2.animate.shift(LEFT * (gap + rect_width)))
        self.wait()
        self.play(GrowFromCenter(completer), Transform(c, adjusted))
        self.wait()