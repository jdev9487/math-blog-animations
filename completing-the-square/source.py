from manim import *

class CreateCircle(Scene):
    def construct(self):
        l1 = Line(LEFT, RIGHT)
        self.add(l1)
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        self.wait(1)
        self.play(MoveAlongPath(circle, l1))